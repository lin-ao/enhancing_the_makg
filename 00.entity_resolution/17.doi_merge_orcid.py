line_count = 1

print("Starting...")

with open("16.doi_orcid_sorted.txt", "r") as inp:
    with open("17.doi_with_merged_orcid.txt", "w") as outp:
        current_doi = ""
        current_orcids = ""
        for line in inp:
            print(line_count)

            doi = line.split("\t")[0].strip()
            name = line.split("\t")[1].strip()
            orcid = line.split("\t")[2].strip()

            if not name.strip() == "":
                if doi == current_doi:
                    current_orcids += (";" + (name + "," + orcid))
                elif current_doi == "":
                    current_doi = doi
                    current_orcids = name + "," + orcid
                else:
                    outp.write(current_doi + "\t" + current_orcids + "\n")
                    current_doi = doi
                    current_orcids = name + "," + orcid

            line_count += 1
    
        outp.write(current_doi + "\t" + current_orcids)

print("Finished.")
