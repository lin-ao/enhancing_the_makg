import itertools

with open("02.knowledge_graph_embeddings/01.tokenized_abstracts_labeled.txt", "r") as f:
    line_count = 1
    fos_dict = {}
    for line in f:
        paperid = line.split("\t")[0]
        fos = line.split("\t")[1].strip()
        fos_dict[paperid] = fos
        print(f"Loading one: {line_count}.")
        line_count += 1

with open("01.field_of_study_classification/02.labels.txt", "r") as f:
    label_mapping = {}
    labels = []
    line_count = 1
    for line in f:
        label_mapping[line.split("\t")[0]] = int(line.strip().split("\t")[2])
        labels.append(line.split("\t")[0])
        print(f"Loading two: {line_count}.")
        line_count += 1

with open("00.entity_resolution/06.authors_with_paper_id.txt", "r") as f:
    with open("09.author_fos.txt", "w") as g:
        line_count = 1
        matrix = [[0 for x in range(19)] for y in range(19)]
        for line in f:
            print(line_count)
            authorid = line.split("\t")[0]
            paperids = line.split("\t")[-1].strip("\n").split(",")
            fos_list = [fos_dict[paperid] for paperid in paperids if paperid in fos_dict]
            if fos_list:
                author_dict = {fos: 0 for fos in labels}
                for item in fos_list:
                    author_dict[item] += 1
                fos_string = ",".join(map(str, [*author_dict.values()]))
                g.write(f"{authorid}\t{fos_string}\n")
                fos_set = set(fos_list)
                if len(fos_set) > 1:
                    fos_combinations = list(itertools.permutations(fos_set, 2))
                    for combination in fos_combinations:
                        matrix[label_mapping[combination[0]]][label_mapping[combination[1]]] += 1
            line_count += 1
        with open("09.author_fos_matrix.txt", "w") as h:
            h.write(str(matrix))
