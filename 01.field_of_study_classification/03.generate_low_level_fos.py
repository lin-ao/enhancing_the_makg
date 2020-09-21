fos_set = set()
with open("02.labels.txt", "r") as f:
    for line in f:
        fos_set.add(line.split("\t")[0])

#Add path to sorted PaperFieldsOfStudy.txt
with open("SortedPaperFieldsOfStudy.txt", "r") as f:
    with open("03.papers_with_direct_labels.txt", "w") as g:
        for line in f:
            if line.split("\t")[1] in fos_set:
                g.write(line)
