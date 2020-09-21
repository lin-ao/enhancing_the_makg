import random

line_count = 1
entity_count = 0
relations_count = 0
entity_dict = {}
relations_dict = {}
with open("00.authors_input.txt", "r") as f:
    for line in f:
        print("Dictionary: " + str(line_count))
        if len(line.split(" ")) > 1:
            sub = line.split(" ")[0].rstrip(">").replace("<http://ma-graph.org/", "")
            pred = line.split(" ")[1].rstrip(">").split("/")[-1].replace("22-rdf-syntax-ns#", "").replace("org#", "")
            obj = " ".join(line.split(" ")[2:]).strip().rstrip(".").strip().replace("^^<http://www.w3.org/2001/XMLSchema#date>", "").replace("^^<http://www.w3.org/2001/XMLSchema#integer>", "").replace("^^<http://www.w3.org/2001/XMLSchema#string>", "").rstrip(">").replace("<http://ma-graph.org/", "").strip('"', '')
            if not sub in entity_dict:
                entity_dict[sub] = entity_count
                entity_count += 1
            if not pred in relations_dict:
                relations_dict[pred] = relations_count
                relations_count += 1
            if not obj in entity_dict:
                entity_dict[obj] = entity_count
                entity_count += 1
        line_count += 1

with open("01.author_entities.dict", "w") as f:
    for item in entity_dict:
        f.write(str(entity_dict[item]) + "\t" + str(item) + "\n")
with open("01.author_relations.dict", "w") as f:
    for item in relations_dict:
        f.write(str(relations_dict[item]) + "\t" + str(item) + "\n")

line_count = 1
with open("00.authors_input.txt", "r") as f:
    with open("01.author_train.tsv", "w") as g:
        with open("01.author_valid.tsv", "w") as h:
            with open("01.author_test.tsv", "w") as i:
                for line in f:
                    print("Splitting: " + str(line_count))
                    if len(line.split(" ")) > 1:
                        sub = line.split(" ")[0].rstrip(">").replace("<http://ma-graph.org/", "")
                        pred = line.split(" ")[1].rstrip(">").split("/")[-1].replace("22-rdf-syntax-ns#", "").replace("org#", "")
                        obj = " ".join(line.split(" ")[2:]).strip().rstrip(".").strip().replace("^^<http://www.w3.org/2001/XMLSchema#date>", "").replace("^^<http://www.w3.org/2001/XMLSchema#integer>", "").replace("^^<http://www.w3.org/2001/XMLSchema#string>", "").rstrip(">").replace("<http://ma-graph.org/", "").strip('"', '')
                        num = random.randint(1, 1000)
                        if num == 999:
                            h.write(str(entity_dict[sub]) + "\t" + str(relations_dict[pred]) + "\t" + str(entity_dict[obj]) + "\n")
                        elif num == 1000:
                            i.write(str(entity_dict[sub]) + "\t" + str(relations_dict[pred]) + "\t" + str(entity_dict[obj]) + "\n")
                        g.write(str(entity_dict[sub]) + "\t" + str(relations_dict[pred]) + "\t" + str(entity_dict[obj]) + "\n")
                    line_count += 1
