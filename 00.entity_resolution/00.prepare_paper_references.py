line_count = 1

print("Starting...")

#Add path to PaperReferences.txt
with open("PaperReferences.txt", "r") as inp:
    with open("00.paper_id_with_merged_references.txt", "w") as outp:
        current_paper_id = ""
        current_references = ""

        for line in inp:
            print(line_count)

            paper_id = line.split("\t")[0].strip()
            author_id = line.split("\t")[1].strip()

            if paper_id == current_paper_id:
                current_references += (";" + author_id)
            elif current_paper_id == "":
                current_paper_id = paper_id
                current_references = author_id
            else:
                list_of_references = ",".join(current_references.split(";")).strip(",")
                outp.write(current_paper_id + "\t" + list_of_references + "\n")
                current_paper_id = paper_id
                current_references = author_id

            line_count += 1

        outp.write(current_paper_id + "\t" + list_of_references + "\n")

print("Finished.")
