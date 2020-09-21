def count_occurence(list_of_objects):
    occurence_dictionary = {}
    for item in list_of_objects:
        if item in occurence_dictionary:
            occurence_dictionary[item] += 1
        else:
            occurence_dictionary[item] = 1
    return occurence_dictionary

papers_properties = ["PaperId", "Rank", "Doi", "DocType", "PaperTitle", "OriginalTitle", "BookTitle", "Year", "Date", "OnlineDate", "Publisher", "JournalId", "ConferenceSeriesId", "ConferenceInstanceId", "Volume", "Issue", "FirstPage", "LastPage", "ReferenceCount", "CitationCount", "EstimatedCitation", "OriginalVenue", "FamilyId", "CreatedDate"]
authors_properties = ["AuthorId", "Rank", "NormalizedName", "DisplayName", "LastKnownAffiliationId", "PaperCount", "paperFamilyCount", "CitationCount", "CreateDate"]

papers_properties_dict = {}
authors_properties_dict = {}


for item in papers_properties:
    papers_properties_dict[item] = 0

#Add file path to Papers.txt
with open("Papers.txt", "r") as inp:
    line_count = 0
    for line in inp:
        line_count += 1
        entries = line.split("\t")
        for index, entry in enumerate(entries):
            if not entry.strip() == "":
                papers_properties_dict[papers_properties[index]] += 1
        print("Paper: " + str(line_count))
with open("00.papers_statistics.txt", "w") as outp:
    outp.write("Total papers: " + str(line_count) + "\n")
    for item in papers_properties_dict:
        outp.write(item + "\t" + str(papers_properties_dict[item]) + "\n")


for item in authors_properties:
    authors_properties_dict[item] = 0

list_of_paper_count = []
list_of_citation_count = []

#Add file path to Authors.txt
with open("Authors.txt", "r") as inp:
    line_count = 0
    for line in inp:
        line_count += 1
        entries = line.split("\t")
        list_of_paper_count.append(entries[5])
        list_of_citation_count.append(entries[6])
        for index, entry in enumerate(entries):
            if not entry.strip() == "":
                authors_properties_dict[authors_properties[index]] += 1
        print("Authors: " + str(line_count))
        
with open("00.authors_statistics.txt", "w") as outp:
    outp.write("Total Authors: " + str(line_count))
    for item in authors_properties_dict:
        outp.write(item + "\t" + str(authors_properties_dict[item]) + "\n")
    print("\nNow calculating paper count...")
    outp.write("Counter for paper count: " + str(count_occurence(list_of_paper_count)) + "\n")
    print("Finished.\nNow calculating citation count...")
    outp.write("Counter for citation count: " + str(count_occurence(list_of_citation_count)))
    print("Finished.")
