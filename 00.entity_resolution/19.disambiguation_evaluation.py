import math
import itertools
from datetime import datetime
from pyjarowinkler import distance


def compare_affiliation(author1, author2):
    affiliation1 = author1.split("\t")[4].strip()
    affiliation2 = author2.split("\t")[4].strip()
    if affiliation1 == "" or affiliation2 == "":
        return False
    else:
        return affiliation1 == affiliation2


def compare_coauthors(author1, author2):
    coauthors1 = set(author1.split("\t")[11].strip().split(","))
    coauthors2 = set(author2.split("\t")[11].strip().split(","))
    if len(coauthors1) == 0 or len(coauthors2) == 0:
        return 0
    else:
        return len(coauthors1.intersection(coauthors2))


def most_frequent(List):
    return sorted(set(List), key=List.count, reverse=True)[:10]


def compare_titles(author1, author2):
    titles1 = author1.split("\t")[12].strip().replace(";", ",").split(",")
    titles2 = author2.split("\t")[12].strip().replace(";", ",").split(",")
    if len(titles1) == 0 or len(titles2) == 0:
        return 0
    else:
        most_freq1 = set(most_frequent(titles1))
        most_freq2 = set(most_frequent(titles2))
        return len(most_freq1.intersection(most_freq2))


def compare_years(author1, author2):
    if author1.split("\t")[13].strip() == "" or author2.split("\t")[13].strip() == "":
        return False
    else:
        years1 = set(map(int, author1.split("\t")[13].strip().split(",")))
        years2 = set(map(int, author2.split("\t")[13].strip().split(",")))
        min_years1 = min(years1)
        max_years1 = max(years1)
        min_years2 = min(years2)
        max_years2 = max(years2)
        return abs(min_years1 - max_years2) < 10 or abs(min_years2 - max_years1) < 10


def compare_journals(author1, author2):
    journals1 = set(author1.split("\t")[14].strip().split(","))
    journals2 = set(author2.split("\t")[14].strip().split(","))
    if len(journals1) == 0 or len(journals2) == 0:
        return 0
    else:
        return len(journals1.intersection(journals2))


def compare_conferences(author1, author2):
    conferences1 = set(author1.split("\t")[15].strip().split(","))
    conferences2 = set(author2.split("\t")[15].strip().split(","))
    if len(conferences1) == 0 or len(conferences2) == 0:
        return 0
    else:
        return len(conferences1.intersection(conferences2))


def self_references(author1, author2):
    paperids1 = set(author1.split("\t")[9].strip().split(","))
    paperids2 = set(author2.split("\t")[9].strip().split(","))
    references1 = set(author1.split("\t")[16].strip().split(","))
    references2 = set(author2.split("\t")[16].strip().split(","))
    return max(len(paperids1.intersection(references2)), len(paperids2.intersection(references1)))


def common_references(author1, author2):
    references1 = set(author1.split("\t")[16].strip().split(","))
    references2 = set(author2.split("\t")[16].strip().split(","))
    if len(references1) == 0 or len(references2) == 0:
        return 0
    else:
        return len(references1.intersection(references2))


def compare_authors(author1, author2):
    score_affiliation = 0
    score_coauthors = 0
    score_titles = 0
    score_years = 0
    score_journals = 0
    score_conferences = 0
    score_self_reference = 0
    score_references = 0
    score = 0

    if compare_affiliation(author1, author2):
        score_affiliation += 5

    if compare_coauthors(author1, author2) == 1:
        score_coauthors += 3
    elif compare_coauthors(author1, author2) == 2:
        score_coauthors += 5
    elif compare_coauthors(author1, author2) > 2:
        score_coauthors += 8

    if compare_titles(author1, author2) == 1:
        score_titles += 3
    elif compare_titles(author1, author2) == 2:
        score_titles += 5
    elif compare_titles(author1, author2) >= 3:
        score_titles += 8

    if compare_years(author1, author2):
        score_years += 3

    if compare_journals(author1, author2) >= 1:
        score_journals += 4

    if compare_conferences(author1, author2) >= 1:
        score_conferences += 4

    if self_references(author1, author2) >= 1:
        score_self_reference += 8

    if common_references(author1, author2) == 1:
        score_references += 2
    elif common_references(author1, author2) == 2:
        score_references += 3
    elif common_references(author1, author2) >= 3:
        score_references += 5

    return [score_affiliation, score_coauthors, score_titles, score_years, score_journals, score_conferences, score_self_reference, score_references]


with open("12.authors_with_references_sorted.txt", "r") as inp:
    with open("19.results_evaluation.txt", "w") as outp:
        with open("19.all_false_positives.txt", "w") as outp2:
            true_positive = 0
            true_negative = 0
            false_positive = 0
            false_negative = 0

            previous_name = ""
            current_authors = []
            true_positives_values = [0,0,0,0,0,0,0,0]
            true_negatives_values = [0,0,0,0,0,0,0,0]
            false_positives_values = [0,0,0,0,0,0,0,0]
            false_negatives_values = [0,0,0,0,0,0,0,0]
            line_count = 1

            for line in inp:
                print(line_count)
                name = line.split("\t")[2].strip()
                if previous_name == "" and len(current_authors) < 500:
                    previous_name = name
                    current_authors.append(line)
                elif distance.get_jaro_distance(str.lower(name), str.lower(previous_name), winkler=True, scaling=0.1) > 0.97 and len(current_authors) < 500:
                    previous_name = name
                    current_authors.append(line)
                else:
                    comparisons = list(itertools.combinations(current_authors, 2))
                    for item in comparisons:
                        if sum(compare_authors(item[0], item[1])) > 10:
                            if item[0].split("\t")[16].strip() == item[1].split("\t")[16].strip():
                                true_positive += 1
                                true_positives_values = [x + y for x, y in zip(true_positives_values, compare_authors(item[0], item[1]))]
                            else:
                                false_positive += 1
                                false_positives_values = [x + y for x, y in zip(false_positives_values, compare_authors(item[0], item[1]))]
                                outp2.write(item[0].strip() + "\t" + item[1].strip() + "\n")                         
                        else:
                            if item[0].split("\t")[16].strip() == item[1].split("\t")[16].strip():
                                false_negative += 1
                                false_negatives_values = [x + y for x, y in zip(false_negatives_values, compare_authors(item[0], item[1]))]
                            else:
                                true_negative += 1
                                true_negatives_values = [x + y for x, y in zip(true_negatives_values, compare_authors(item[0], item[1]))]
                    previous_name = ""
                    current_authors = []

                line_count += 1

            total_comparisons = true_positive + false_positive + true_negative + false_negative
            total_positives = true_positive + false_negative
            total_negatives = true_negative + false_positive

            precision = true_positive / (true_positive + false_positive)
            recall = true_positive / (true_positive + false_negative)
            accuracy = (true_positive + true_negative) / (true_positive + false_positive + true_negative + false_negative)

            outp.write("Total comparisons: " + str(total_comparisons) + "\n")
            outp.write("Total positives: " + str(total_positives) + "\n")
            outp.write("Total negatives: " + str(total_negatives) + "\n\n")
            outp.write("True positives: " + str(true_positive) + "\n")
            outp.write("False positives: " + str(false_positive) + "\n")
            outp.write("True negatitves: " + str(true_negative) + "\n")
            outp.write("False negatives: " + str(false_negative) + "\n\n")
            outp.write("Precision: " + str(precision) + "\n")
            outp.write("Recall: " + str(recall) + "\n")
            outp.write("Accuracy: " + str(accuracy) + "\n\n")
            outp.write("Average true positive: " + str([value/max(true_positive, 1) for value in true_positives_values]) + "\n")
            outp.write("Average true negative: " + str([value/max(true_negative, 1) for value in true_negatives_values]) + "\n")
            outp.write("Average false positive: " + str([value/max(false_positive, 1) for value in false_positives_values]) + "\n")
            outp.write("Average false negative: " + str([value/max(false_negative, 1) for value in false_negatives_values]) + "\n")

