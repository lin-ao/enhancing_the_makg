dict_of_paperids = {}
line_count = 1

print("Starting...")

with open("04.author_id_with_merged_paper_id.txt", "r") as inp:
    for line in inp:
        print("Loading: " + str(line_count))

        author_id = line.split("\t")[0].strip()
        paper_ids = line.split("\t")[1].strip()
        dict_of_paperids[author_id] = paper_ids

        line_count += 1

line_count = 1

#Add path to Authors.txt
with open("00.Authors.txt", "r") as inp:
    with open("06.authors_with_paper_id.txt", "w") as outp:
        for line in inp:
            print("Searching: " + str(line_count))

            current_author = line.split("\t")[0].strip()
            try:
                outp.write(line.strip("\n") + "\t" + dict_of_paperids[current_author] + "\n")
            except KeyError:
                outp.write(line.strip("\n") + "\t\n")

            line_count += 1

print("Finished.")
