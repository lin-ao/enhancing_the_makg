id_mapping = {}
with open("13.all_positives.txt", "r") as f:
    for line in f:
        id_mapping[line.split("\t")[0].strip()] = line.split("\t")[1].strip()
line_count = 1

#Add path to PaperAuthorAffiliations.txt
with open("PaperAuthorAffiliations.txt", "r") as f:
    with open("14.PaperAuthorAffiliations_new.txt", "w") as g:
        for line in f:
            print("PaperAuthorAffiliations: " + str(line_count))
            author_id = line.split("\t")[1].strip()
            if author_id in id_mapping:
                g.write(line.replace(author_id, id_mapping[author_id]))
            else:
                g.write(line)
            line_count += 1
line_count = 1
with open("13.disambiguated_file.txt", "r") as f:
    with open("14.Authors_new.txt", "w") as g:
        for line in f:
            print("Authors: " + str(line_count))
            items = line.strip().split("\t")
            g.write("\t".join(items[0:9]) + "\n")
            line_count += 1
