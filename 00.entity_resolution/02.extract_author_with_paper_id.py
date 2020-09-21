line_count = 0

print("Starting...")

#Add path to PaperAuthorAffiliations.txt
with open("PaperAuthorAffiliations.txt", "r") as inp:
    with open("02.author_id_with_paper_id.txt", "w") as outp:
        for line in inp:
            line_count += 1

            paper_id = line.split("\t")[0].strip()
            author_id = line.split("\t")[1].strip()
            outp.write(author_id + "\t" + paper_id + "\n")

            print(line_count)

print("Finished.")
