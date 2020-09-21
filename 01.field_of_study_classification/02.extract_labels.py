#Add path to FieldsOfStudy.txt
with open("FieldsOfStudy.txt", "r") as f:
    with open("02.labels.txt", "w") as g:
        index = 0
        for line in f:
            id = line.split("\t")[0]
            name = line.split("\t")[3]
            level = line.split("\t")[5]
            if level == "0":
                g.write(f"{id}\t{name}\t{index}\n")
                index += 1