dict_of_titles = {}
line_count = 1

print("Starting...")

#Add path to Papers.txt
with open("Papers.txt", "r") as inp:
    for line in inp:
        print("Loading: " + str(line_count))

        paper_id = line.split("\t")[0].strip()
        paper_title = line.split("\t")[4].strip()
        book_title = line.split("\t")[6].strip()
        dict_of_titles[paper_id] = paper_title + book_title

        line_count += 1

line_count = 1

with open("08.authors_with_co_authors.txt", "r") as inp:
    with open("09.authors_with_titles.txt", "w") as outp:
        for line in inp:
            print("Searching: " + str(line_count))

            paper_ids = line.split("\t")[9].strip().split(",")
            titles = []
            for paper_id in paper_ids:
                try:
                    titles.append(dict_of_titles[paper_id])
                except KeyError:
                    pass
            outp.write(line.strip("\n") + "\t" + ",".join(titles) + "\n")

            line_count += 1

print("Finished.")

