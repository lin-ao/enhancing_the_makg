with open("/pfs/work7/workspace/scratch/utdkf-ws_lin-0/0.data/0.mag_20200619/advanced/PaperRecommendations.txt", "r") as f:
    with open("17.PaperRecommendations.nt", "w") as g:
        for line in f:
            PaperId, RecommendedPaperId, Score = line.strip("\n").split("\t")
            g.write(f'<http://ma-graph.org/entity/{PaperId}> <http://ma-graph.org/property/recommends> <http://ma-graph.org/entity/{RecommendedPaperId}> .\n')