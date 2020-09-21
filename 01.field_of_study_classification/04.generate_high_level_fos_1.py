fos_dict = {}
paper_labels = set()

with open("02.labels.txt", "r") as f:
    for line in f:
        paper_labels.add(line.split("\t")[0].strip())

def find_top_fos(fos, fos_dict, paper_labels):
    output =  {fos}
    while any(f in fos_dict for f in output):
        for f in {f for f in output if f in fos_dict}:
            output.update(fos_dict[f])
            output.remove(f)
    return output.intersection(paper_labels)

line_count = 1
#Add path to FieldOfStudyChildren.txt
with open("FieldOfStudyChildren.txt", "r") as f:
    for line in f:
        child_fos = line.split("\t")[1].strip()
        parent_fos = line.split("\t")[0].strip()
        if child_fos in fos_dict:
            fos_dict[child_fos].add(parent_fos)
        else:
            fos_dict[child_fos] = {parent_fos}

#Add path to sorted PaperFieldsOfStudy.txt
with open("SortedPaperFieldsOfStudy", "r") as f:
    with open("04.papers_top_level_labels.txt", "w") as g:
        for line in f:
            print(line_count)
            fos = line.split("\t")[1].strip()
            for f in find_top_fos(fos, fos_dict, paper_labels):
                g.write(line.replace(fos, f))
            line_count += 1 

