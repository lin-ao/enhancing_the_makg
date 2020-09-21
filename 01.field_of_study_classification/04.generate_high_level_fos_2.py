import operator

line_count = 1
with open("04.papers_top_level_labels.txt", "r") as f:
    with open("04.papers_with_indirect_labels.txt", "w") as g:
        current_paper = ""
        paper_dict = {}
        paper_count = {}
        for line in f:
            print(line_count)
            paperid = line.split("\t")[0]
            fos = int(line.split("\t")[1])
            score = float(line.split("\t")[2].strip())
            if current_paper == "":
                current_paper = paperid
                paper_dict[fos] = score
                paper_count[fos] = 1
            elif paperid == current_paper:
                try:
                    paper_dict[fos] += score
                    paper_count[fos] += 1
                except KeyError:
                    paper_dict[fos] = score
                    paper_count[fos] = 1
            else:
                g.write(current_paper + "\t" + str(max(paper_dict.items(), key=operator.itemgetter(1))[0]) + "\t" + str(max(paper_dict.items(), key=operator.itemgetter(1))[1]) + "\n")
                current_paper = paperid
                paper_dict.clear()
                paper_count.clear()
                paper_dict[fos] = score
                paper_count[fos] = 1
            line_count += 1
        for item in paper_dict:
            g.write(current_paper + "\t" + str(item) + "\t" + str(paper_dict[item]/max((paper_count[item]-1), 1)) + "\n")
