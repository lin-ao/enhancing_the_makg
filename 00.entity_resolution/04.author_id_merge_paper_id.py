line_count = 1

print("Starting...")

with open("02.author_id_with_paper_id_sorted.txt", "r") as inp:
    with open("04.author_id_with_merged_paper_id.txt", "w") as outp:
        current_author_id = ""
        current_papers = ""

        for line in inp:
            print(line_count)

            paper_id = line.split("\t")[1].strip()
            author_id = line.split("\t")[0].strip()

            if author_id == current_author_id:
                current_papers += (";" + paper_id)
            elif current_author_id == "":
                current_author_id = author_id
                current_papers = paper_id
            else:
                list_of_papers = ",".join(current_papers.split(";")).strip(",")
                outp.write(current_author_id + "\t" + list_of_papers + "\n")
                current_author_id = author_id
                current_papers = paper_id

            line_count += 1

        outp.write(current_author_id + "\t" + list_of_papers + "\n")
        
print("Finished.")
