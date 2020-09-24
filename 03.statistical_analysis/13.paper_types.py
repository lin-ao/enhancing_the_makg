type_dict = {}
#Add file path for Papers.txt
with open("Papers.txt", "r") as f:
    with open("13.paper_types.txt", "w") as g:
        for line in f:
            doctype = line.split("\t")[3]
            try:
                type_dict[doctype] += 1
            except KeyError:
                type_dict[doctype] = 1
        g.write(str(type_dict))