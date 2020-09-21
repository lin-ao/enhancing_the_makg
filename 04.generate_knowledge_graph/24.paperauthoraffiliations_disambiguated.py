with open("/pfs/work7/workspace/scratch/utdkf-ws_lin-0/mag/14.PaperAuthorAffiliations_new.txt", "r") as f:
    with open("06.PaperAuthorAffiliations.nt", "w") as g:
        for line in f:
            PaperId = line.split("\t")[0]
            AuthorId = line.split("\t")[1]
            g.write(f'<http://ma-graph.org/entity/{AuthorId}> <http://purl.org/dc/terms/creator> <http://ma-graph.org/entity/{PaperId}> .\n')
            