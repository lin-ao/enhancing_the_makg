def label_fos(input_file, output_file):
    with open("02.labels.txt", "r") as f:
        label_dict = {}
        for line in f:
            label_dict[line.strip().split("\t")[2]] = line.split("\t")[0]
    with open(f"{input_file}.txt", "r") as f:
        label_list = []
        for line in f:
            label_list.append(line.strip())
    with open(output_file, "a") as f:
        with open(input_file, "r") as g:
            for index, line in enumerate(g):
                paperid = line.split("\t")[0]
                f.write(f"{paperid}\t{label_dict[label_list[index]]}\n")

f = open("10.paperid_with_fos.txt", "w")
f.close()

label_fos("01.tokenized_abstracts.txt", "10.paperid_with_fos.txt")
