with open("01.field_of_study_classification/00.paper_abstracts.txt", "r") as f:
    with open("20.PaperAbstracts.nt", "w") as g:
        for line in f:
            PaperId, PaperAbstract = line.strip("\n").split("\t")
            g.write(f'<http://ma-graph.org/entity/{PaperId}> <purl.org/dc/terms/abstract> "{PaperAbstract}"^^<http://www.w3.org/2001/XMLSchema#string> .\n')