import math
import itertools
from datetime import datetime
from pyjarowinkler import distance

#Parameters
score_affiliation = 1
score_coauthors_1 = 3
score_coauthors_2 = 5
score_coauthors_3 = 8
score_titles_1 = 3
score_titles_2 = 5
score_titles_3 = 8
score_years = 3
score_journals = 3
score_conferences = 3
score_self_reference = 8
score_references_1 = 2
score_references_2 = 3
score_references_3 = 5
threshold_matching = 10
threshold_blocking = 0.95
scaling_factor = 0.1
max_block_size = 500


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
    if len(paperids1) == 0 or len(paperids2) == 0 or len(references1) == 0 or len(references2) == 0:
        return 0
    else:
        return max(len(paperids1.intersection(references2)), len(paperids2.intersection(references1)))


def common_references(author1, author2):
    references1 = set(author1.split("\t")[16].strip().split(","))
    references2 = set(author2.split("\t")[16].strip().split(","))
    if len(references1) == 0 or len(references2) == 0:
        return 0
    else:
        return len(references1.intersection(references2))


def compare_authors(author1, author2):
    score = 0
    if compare_affiliation(author1, author2):
        score += score_affiliation

    if compare_coauthors(author1, author2) == 1:
        score += score_coauthors_1
    elif compare_coauthors(author1, author2) == 2:
        score += score_coauthors_2
    elif compare_coauthors(author1, author2) > 2:
        score += score_coauthors_3

    if compare_titles(author1, author2) == 1:
        score += score_titles_1
    elif compare_titles(author1, author2) == 2:
        score += score_titles_2
    elif compare_titles(author1, author2) >= 3:
        score += score_titles_3

    if compare_years(author1, author2):
        score += score_years

    if compare_journals(author1, author2) >= 1:
        score += score_journals

    if compare_conferences(author1, author2) >= 1:
        score += score_conferences

    if self_references(author1, author2) >= 1:
        score += score_self_reference

    if common_references(author1, author2) == 1:
        score += score_references_1
    elif common_references(author1, author2) == 2:
        score += score_references_2
    elif common_references(author1, author2) >= 3:
        score += score_references_3

    return score


def get_id(author):
    return author.split("\t")[0]


def earlier_date(author1, author2):
    date_object1 = datetime.strptime(author1[8], "%Y-%m-%d")
    date_object2 = datetime.strptime(author2[8], "%Y-%m-%d")
    earliest = min(date_object1, date_object2)
    stringified = "-".join([str(earliest.year),
                            str(earliest.month), str(earliest.day)])
    return stringified


def latest_affiliation(author1, author2):
    date_object1 = datetime.strptime(author1[8], "%Y-%m-%d")
    date_object2 = datetime.strptime(author2[8], "%Y-%m-%d")
    if date_object1 < date_object2:
        return author2[4]
    else:
        return author1[4]


def add_paper_count(author1, author2):
    return str(int(author1[5]) + int(author2[5]))

def add_paper_family_count(author1, author2):
    return str(int(author1[6]) + int(author2[6]))

def add_citation_count(author1, author2):
    return str(int(author1[7]) + int(author2[7]))


def merge_authors(tuple_of_authors):
    author1 = tuple_of_authors[0].strip("\n").split("\t")
    author2 = tuple_of_authors[1].strip("\n").split("\t")
    output = "\t".join(author1[0:4]) + "\t" + latest_affiliation(author1, author2) + "\t" + add_paper_count(author1, author2) + "\t" + add_paper_family_count(author1, author2) + "\t" + add_citation_count(author1, author2) + "\t" + earlier_date(author1, author2) + "\t" + (author1[9]+","+author2[9]).strip(",") + "\t" + (author1[10]+","+author2[10]).strip(",") + "\t" + (author1[11] +","+author2[11]).strip(",") + "\t" + (author1[12]+","+author2[12]).strip(",")  + "\t" + (author1[13]+","+author2[13]).strip(",")  + "\t" + (author1[14]+","+author2[14]).strip(",")  + "\t" + (author1[15]+","+author2[15]).strip(",")  + "\t" + (author1[16]+","+author2[16]).strip(",")
    return output


def add_to_mapping(dict_of_maps, entry1, entry2):
    if entry2 not in dict_of_maps:
        dict_of_maps[entry1] = entry2
        return dict_of_maps
    else:
        return add_to_mapping(dict_of_maps, entry1, dict_of_maps[entry2])


def disambiguate(list_of_authors, result, positive, negative):
    author_dictionary = {get_id(author): author.strip("\n") for author in list_of_authors}
    author_list = [get_id(author) for author in list_of_authors]
    mapping = {}
    result = result.copy()
    comparisons = list(itertools.combinations(author_list, 2))
    for item in comparisons:
        try:
            if compare_authors(author_dictionary[item[0]], author_dictionary[item[1]]) > threshold_matching:
                positive += 1
                if item[0] not in mapping:
                    mapping = add_to_mapping(mapping, item[1], item[0])
                    result = add_to_mapping(result, item[1], item[0])
                    author_dictionary[item[0]] = merge_authors((author_dictionary[item[0]], author_dictionary[item[1]]))
                    del author_dictionary[item[1]]
                else:
                    author_dictionary[mapping[item[0]]] = merge_authors((author_dictionary[mapping[item[0]]], author_dictionary[item[1]]))
                    mapping = add_to_mapping(mapping, item[1], item[0])
                    result = add_to_mapping(result, item[1], item[0])
                    del author_dictionary[item[1]]
            else:
                negative += 1
        except KeyError:
            pass
    return author_dictionary, result, positive, negative
    

with open("12.authors_with_references_sorted.txt", "r") as inp:
    with open("13.results.txt", "w") as outp:
        with open("13.all_positives.txt", "w") as outp2:
            with open("13.disambiguated_file.txt", "w") as outp3:
                positive = 0
                negative = 0

                previous_name = ""
                current_authors = []

                line_count = 1

                for line in inp:
                    print("Disambiguation: " + str(line_count))

                    name = line.split("\t")[2].strip()
                    if previous_name == "" and len(current_authors) < max_block_size:
                        previous_name = name
                        current_authors.append(line)
                    elif distance.get_jaro_distance(str.lower(name), str.lower(previous_name), winkler=True, scaling=scaling_factor) > threshold_blocking and len(current_authors) < max_block_size:
                        previous_name = name
                        current_authors.append(line)
                    else:
                        result = {}                            
                        authors, result, positive, negative = disambiguate(current_authors, result, positive, negative)
                        previous_name = name
                        current_authors = [line]
                        for item in authors:
                            outp3.write(authors[item] + "\n")
                        for item in result:
                            outp2.write(item + "\t" + result[item] + "\n")
			
                    line_count += 1

                result = {} 
                authors, result, positive, negative = disambiguate(current_authors, result, positive, negative)
                for item in authors:
                    outp3.write(authors[item] + "\n")
                for item in result:
                    outp2.write(item + "\t" + result[item] + "\n")

        total_comparisons = positive + negative

        outp.write("Total comparisons: " + str(total_comparisons) + "\n")
        outp.write("Total positives: " + str(positive) + ": " + str(positive/total_comparisons) + "\n")
        outp.write("Total negatives: " + str(negative) + ": " + str(negative/total_comparisons))
