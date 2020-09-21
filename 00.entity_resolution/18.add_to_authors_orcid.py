from pyjarowinkler import distance

dict_of_orcids = {}
line_count = 1

print("Starting...")

with open("17.doi_with_merged_orcid.txt", "r") as inp:
    for line in inp:
        print("Loading: " + str(line_count))

        doi = line.split("\t")[0].strip()
        orcid = line.split("\t")[1].strip()
        dict_of_orcids[doi] = orcid

        line_count += 1

line_count = 1

with open("12.authors_with_references_sorted.txt", "r") as inp:
    with open("18.authors_with_orcid.txt", "w") as outp:
        for line in inp:
            print("Searching: " + str(line_count))

            name = line.split("\t")[3].strip()
            dois = line.split("\t")[9].strip().split(";")
            orcids = set()
            for doi in dois:
                try:
                    found_orcids = dict_of_orcids[doi].split(";")
                    for orcid in found_orcids:
                        if distance.get_jaro_distance(str.lower(name), str.lower(orcid.split(",")[0]), winkler=True, scaling=0.1)>0.9:
                                orcids.update([orcid.split(",")[1].strip()])
                except KeyError:
                    pass
            outp.write(line.strip("\n") + "\t" + ",".join(orcids).strip() + "\n")
            
            line_count += 1

print("Finished.")

