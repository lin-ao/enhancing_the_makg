with open("/pfs/work7/workspace/scratch/utdkf-ws_lin-0/3.field_of_study/4.keyword_extraction/keywords_extraction/paper_keywords.txt", "r") as f:
    with open("21.PaperTags.nt", "w") as g:
        for line in f:
            PaperId = line.split("\t")[0]
            PaperTag = line.strip("\n").split("\t")[3]
            g.write(f'<http://ma-graph.org/entity/{PaperId}> <http://ma-graph.org/property/hasTag> "{PaperTag}"^^<http://www.w3.org/2001/XMLSchema#string> .\n')