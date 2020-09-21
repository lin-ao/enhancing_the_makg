paper_label_dict = {}
with open("05.paper_journal_labels.txt", "r") as f:
    for line in f:
        paper_label_dict[line.split("\t")[0].strip()] = line.split("\t")[1].strip()

with open("00.paper_abstracts.txt", "r") as f:
    with open("05.papers_with_journal_labels.txt", "w") as g:
        for line in f:
            items = line.strip().split("\t")
            if items[0] in paper_label_dict:
                g.write(items[0] + "\t" + items[1] + "\t" + paper_label_dict[items[0]] + "\n")
