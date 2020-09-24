with open("PaperUrls.txt", "r") as f:
    with open("11.PaperUrls.nt", "w") as g:
        for line in f:
            PaperId = line.split("\t")[0]
            SourceUrl = line.split("\t")[2]
            g.write(f'<http://ma-graph.org/entity/{PaperId}> <http://purl.org/spar/fabio/hasURL> "{SourceUrl}"^^<http://www.w3.org/2001/XMLSchema#anyURI> .\n')
            