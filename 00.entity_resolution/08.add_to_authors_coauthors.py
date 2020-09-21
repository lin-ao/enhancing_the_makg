dict_of_coauthors = {}
line_count = 1

print("Starting...")

with open("05.paper_id_with_merged_author_id.txt", "r") as inp:
    for line in inp:
        print("Loading: " + str(line_count))
        paper_id = line.split("\t")[0].strip()
        author_ids = line.split("\t")[1].strip()
        dict_of_coauthors[paper_id] = author_ids
        line_count+= 1

number_of_papers = 0
number_of_papers_with_coauthors = 0
number_of_mismatches = 0
line_count = 1

with open("07.authors_with_paper_doi.txt", "r") as inp:
    with open("08.authors_with_co_authors.txt", "w") as outp:
        for line in inp:
            print("Searching: " + str(line_count))
            author_id = line.split("\t")[0].strip()
            paper_ids = line.split("\t")[9].strip().split(",")
            co_authors = set()
            for paper_id in paper_ids:
                number_of_papers += 1
                try:
                    co_authors.update(dict_of_coauthors[paper_id].split(","))
                    number_of_papers_with_coauthors += 1
                    try: 
                        co_authors.remove(author_id)
                    except KeyError:
                        number_of_mismatches += 1
                except KeyError:
                    pass            
            outp.write(line.strip("\n") + "\t" + ",".join(co_authors) + "\n")

            line_count += 1

print("Total number of papers: " + str(number_of_papers) + ". With coauthors :" + str(number_of_papers_with_coauthors) + " . With number of mismatches: " + str(number_of_mismatches))

print("Finished.")
