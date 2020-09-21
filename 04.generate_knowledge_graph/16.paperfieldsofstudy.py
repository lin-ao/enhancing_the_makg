with open("/pfs/work7/workspace/scratch/utdkf-ws_lin-0/0.data/0.mag_20200619/advanced/PaperFieldsOfStudy.txt", "r") as f:
    with open("16.PaperFieldsOfStudy.nt", "w") as g:
        for line in f:
            PaperId, FieldOfStudyId, Score = line.strip("\n").split("\t")
            g.write(f'<http://ma-graph.org/entity/{PaperId}> <http://purl.org/spar/fabio/hasDiscipline> <http://ma-graph.org/entity/{FieldOfStudyId}> .\n')