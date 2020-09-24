with open("01.field_of_study_classification/11.paper_keywords.txt", "r") as f:
    with open("21.PaperTags.nt", "w") as g:
        for line in f:
            PaperId = line.split("\t")[0]
            PaperTag = line.strip("\n").split("\t")[3]
            g.write(f'<http://ma-graph.org/entity/{PaperId}> <http://ma-graph.org/property/hasTag> "{PaperTag}"^^<http://www.w3.org/2001/XMLSchema#string> .\n')