labels_mapping = {}
with open("02.labels.txt", "r") as f:
    for line in f:
        labels_mapping[line.split("\t")[1].strip().lower()] = line.split("\t")[2].strip()

labels_list = [*labels_mapping.keys()]

#Add path to Journals.txt
with open("Journals.txt", "r") as f:
    with open("05.journals_label.txt", "w") as g:
        for line in f:
            journal = line.split("\t")[3].strip().lower()
            for label in labels_list:    
                if " " + label + " " in journal or " " + label + "s " in journal:
                    g.write(line.strip() + "\t" + labels_mapping[label] + "\n")
