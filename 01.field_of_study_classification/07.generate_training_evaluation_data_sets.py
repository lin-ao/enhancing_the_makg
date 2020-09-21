with open("05.papers_with_journal_labels.txt", "r") as f:
    with open("train.csv", "w") as g:
        with open("eval.csv", "w") as h:    
            fos_dict = {}
            line_count = 1
            for line in f:
                print(line_count)
                fos = line.split("\t")[2].strip()
                try:
                    if fos_dict[fos] < 2000:
                        h.write(line.split("\t")[1] + " ," + fos + "\n")
                        fos_dict[fos] += 1
                    elif fos_dict[fos] < 22000:
                        g.write(line.split("\t")[1] + " ," + fos + "\n")
                        fos_dict[fos] += 1
                    else:
                        pass
                except KeyError:
                    h.write(line.split("\t")[1] + " ," + fos + "\n")
                    fos_dict[fos] = 1
                line_count += 1
for item in fos_dict:
    print(str(item) + "\t" + str(fos_dict[item]-2000))
