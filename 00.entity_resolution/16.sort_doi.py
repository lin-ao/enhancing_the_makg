list_of_doi_orcid = []
line_count = 1

print("Starting...")

with open("15.orcid_title_doi.txt", "r") as inp:  
    for line in inp:
        print(line_count)

        try:
            orcid, name, title, doi = map(str.strip, line.split("\t"))
            if not doi == "" and not name == "":
                list_of_doi_orcid.append((doi.replace("(", "").replace(")", "").replace("http://dx.doi.org/", ""), name.strip(), orcid.strip()))
        except ValueError:
            pass

        line_count += 1

print("Start sorting...")
list_of_doi_orcid.sort(key=lambda tup: tup[0])
print("Finished sorting.")

with open("16.doi_orcid_sorted.txt", "w") as outp:
    for item in list_of_doi_orcid:
        for name in item[1].split(";"):
            outp.write(item[0] + "\t" + name + "\t" + item[2] + "\n")

print("Finished.")
