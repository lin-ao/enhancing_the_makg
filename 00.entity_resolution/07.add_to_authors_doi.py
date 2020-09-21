dict_of_dois = {}
line_count = 1

print("Starting...")

with open("01.paper_id_with_doi_sorted.txt", "r") as inp:
    for line in inp:
        print("Loading: " + str(line_count))

        paper_id = line.split("\t")[0].strip()
        doi = line.split("\t")[1].strip()
        dict_of_dois[paper_id] = doi

        line_count += 1

line_count = 1

with open("06.authors_with_paper_id.txt", "r") as inp:
    with open("07.authors_with_paper_doi.txt", "w") as outp:
        for line in inp:
            print("Searching: " + str(line_count))

            paper_ids = line.split("\t")[9].strip()
            current_dois = []
            for current_id in paper_ids.split(","):
                try:
                    current_dois.append(dict_of_dois[current_id])
                except KeyError:
                    pass
            outp.write(line.strip("\n") + "\t" + ",".join(current_dois) + "\n")

            line_count += 1

print("Finished.")
