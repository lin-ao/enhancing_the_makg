with open("PaperReferences.txt", "r") as f:
    with open("08.PaperReferences.nt", "w") as g:
        for line in f:
            PaperId = line.split("\t")[0].strip()
            PaperReferenceId = line.split("\t")[1].strip()
            g.write(f'<http://ma-graph.org/entity/{PaperId}> <http://purl.org/spar/cito/cites> <http://ma-graph.org/entity/{PaperReferenceId}> .\n')
            