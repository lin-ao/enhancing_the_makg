with open("01.field_of_study_classification/03.papers_with_direct_labels.txt", "r") as f:
    fos_dict = {}
    for line in f:
        paperid = line.split("\t")[0]
        fos = line.split("\t")[1]
        fos_dict[paperid] = fos

with open("01.field_of_study_classification/02.labels.txt", "r") as f:
    labels = set()
    for line in f:
        labels.add(line.split("\t")[0])

for item in labels:
    f = open(f"03.field_of_study_over_time/{item}.txt", "w")
    f.close()

#Add file path for Papers.txt
with open("Papers.txt", "r") as f:
    for line in f:
        paperid = line.split("\t")[0]
        try:
            with open(f"03.field_of_study_over_time/{fos_dict[paperid]}.txt", "a") as g:
                g.write(line)
        except KeyError:
            pass
        

