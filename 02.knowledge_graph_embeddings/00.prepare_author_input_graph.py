pred_list = ["<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>", "<http://xmlns.com/foaf/0.1/name>", "<http://www.w3.org/ns/org#memberOf>", "<http://ma-graph.org/property/paperCount>", "<http://ma-graph.org/property/citationCount>"]

#Add file path to Authors.nt
with open("00.authors_input.txt", "w") as g:
    with open("Authors.nt", "r") as f:
        for line in f: 
            pred = line.split(" ")[1]
            if pred in pred_list:
                g.write(line)
        
