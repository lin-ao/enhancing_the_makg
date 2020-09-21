paper_label_dict = {}
label_total_count = {}
label_matching_count = {}
with open("02.labels.txt", "r") as f:
    for line in f:
        paper_label_dict[line.split("\t")[0].strip()] = line.split("\t")[2].strip()
        label_total_count[line.split("\t")[2].strip()] = 0
        label_matching_count[line.split("\t")[2].strip()] = 0

line_count = 1
journal_label = {}
mag_label = {}
with open("05.papers_with_journal_labels.txt", "r") as f:
    for line in f:
        print("Loading Journal: " + str(line_count))
        paper_id = line.split("\t")[0]
        label = line.strip().split("\t")[2]
        journal_label[paper_id] = label
        line_count += 1

line_count = 1
#Edit the following data path depending on which labels you want to evaluate
with open("03.papers_with_direct_labels.txt", "r") as f:
    for line in f:
        print("Loading MAG: " + str(line_count))
        paper_id = line.split("\t")[0]
        label = line.split("\t")[1]
        mag_label[paper_id] = label
        line_count += 1

line_count = 1
total_count = 0
matching = 0
for item in journal_label:
    print("Comparing: " + str(line_count))
    try:
        if journal_label[item] == mag_label[item]:
            matching += 1
            label_matching_count[journal_label[item]] += 1
        total_count += 1
        label_total_count[journal_label[item]] += 1
    except KeyError:
        pass
    line_count += 1

print("Total: " + str(total_count))
print("Matching: " + str(matching))
for item in label_matching_count:
    print("Label: " + item + " Total: " + str(label_total_count[item]) + " Matching: " + str(label_matching_count[item]))
