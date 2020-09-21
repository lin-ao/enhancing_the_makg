with open("/pfs/work7/workspace/scratch/utdkf-ws_lin-0/0.data/0.mag_20200619/mag/PaperUrls.txt", "r") as f:
    with open("11.PaperUrls.nt", "w") as g:
        for line in f:
            PaperId = line.split("\t")[0]
            SourceUrl = line.split("\t")[2]
            g.write(f'<http://ma-graph.org/entity/{PaperId}> <http://purl.org/spar/fabio/hasURL> "{SourceUrl}"^^<http://www.w3.org/2001/XMLSchema#anyURI> .\n')
            