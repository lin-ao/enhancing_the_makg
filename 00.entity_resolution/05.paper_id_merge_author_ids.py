line_count = 1

print("Starting...")

with open("03.paper_id_with_author_id_sorted.txt", "r") as inp:
    with open("05.paper_id_with_merged_author_id.txt", "w") as outp:
        current_paper_id = ""
        current_authors = ""

        for line in inp:
            print(line_count)

            paper_id = line.split("\t")[0].strip()
            author_id = line.split("\t")[1].strip()

            if paper_id == current_paper_id:
                current_authors += (";" + author_id)
            elif current_paper_id == "":
                current_paper_id = paper_id
                current_authors = author_id
            else:
                list_of_authors = ",".join(current_authors.split(";")).strip(",")
                outp.write(current_paper_id + "\t" + list_of_authors + "\n")
                current_paper_id = paper_id
                current_authors = author_id

            line_count += 1

        outp.write(current_paper_id + "\t" + list_of_authors + "\n")

print("Finished.")
