journal_labels = {}
with open("05.journals_label.txt", "r") as f:
    for line in f:
        journal_labels[line.split("\t")[0].strip()] = line.split("\t")[10].strip()

#Add path to Papers.txt
line_count = 1
with open("Papers.txt", "r") as f:
    with open("05.paper_journal_labels.txt", "w") as g:
        for line in f:
            print(line_count)
            paper_id = line.split("\t")[0].strip()
            journal_id = line.split("\t")[10].strip()
            if journal_id in journal_labels:
                g.write(paper_id + "\t" + journal_labels[journal_id] + "\n")
            line_count += 1
