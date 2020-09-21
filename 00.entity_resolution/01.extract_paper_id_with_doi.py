list_of_paper_id = []
line_count = 0

print("Starting...")

#Add path to Papers.txt
with open("Papers.txt", "r") as inp:
    for line in inp:
        line_count += 1

        paper_id = line.split("\t")[0].strip()
        doi = line.split("\t")[2].strip()
        if not doi == "":
            list_of_paper_id.append((int(paper_id), doi))
            
        print(line_count)

    print("Start sorting...")
    list_of_paper_id.sort(key=lambda tup: tup[0])
    print("Finished sorting.")

print("Start writing...")
with open("01.paper_id_with_doi_sorted.txt", "w") as outp:
    for item in list_of_paper_id:
        outp.write(str(item[0]) + "\t" + item[1] + "\n")

print("Finished.")
