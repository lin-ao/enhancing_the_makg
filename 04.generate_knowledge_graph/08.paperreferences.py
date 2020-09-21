with open("/pfs/work7/workspace/scratch/utdkf-ws_lin-0/0.data/0.mag_20200619/mag/PaperReferences.txt", "r") as f:
    with open("08.PaperReferences.nt", "w") as g:
        for line in f:
            PaperId = line.split("\t")[0].strip()
            PaperReferenceId = line.split("\t")[1].strip()
            g.write(f'<http://ma-graph.org/entity/{PaperId}> <http://purl.org/spar/cito/cites> <http://ma-graph.org/entity/{PaperReferenceId}> .\n')
            