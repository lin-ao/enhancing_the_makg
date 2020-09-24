with open("PaperRecommendations.txt", "r") as f:
    with open("17.PaperRecommendations.nt", "w") as g:
        for line in f:
            PaperId, RecommendedPaperId, Score = line.strip("\n").split("\t")
            g.write(f'<http://ma-graph.org/entity/{PaperId}> <http://ma-graph.org/property/recommends> <http://ma-graph.org/entity/{RecommendedPaperId}> .\n')