dict_of_references = {}
line_count = 1

print("Starting...")

with open("00.paper_id_with_merged_references.txt", "r") as inp:
    for line in inp:
        print("Loading: " + str(line_count))

        paper_id = line.split("\t")[0].strip()
        references = line.split("\t")[1].strip()
        dict_of_references[paper_id] = references
        line_count += 1

line_count = 1
found = 0
not_found = 0

with open("11.authors_with_journal_and_conference.txt", "r") as inp:
    with open("12.authors_with_references.txt", "w") as outp:
        for line in inp:
            print("Searching: " + str(line_count))

            paper_ids = line.split("\t")[9].strip().split(",")
            references = set()
            for paper_id in paper_ids:
                try:
                    references.update(dict_of_references[paper_id].split(","))
                except KeyError:
                    pass
            outp.write(line.strip("\n") + "\t" + ",".join(references) + "\n")

            line_count += 1

print("Finished.")
