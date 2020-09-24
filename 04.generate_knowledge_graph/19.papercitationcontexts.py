with open("PaperCitationContexts.txt", "r") as f:
    with open("19.PaperCitationContexts.nt", "w") as g:
        for line in f:
            PaperId, PaperReferenceId, CitationContext = line.strip("\n").split("\t")
            g.write(f'<http://ma-graph.org/entity/{PaperId}-{PaperReferenceId}> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ma-graph.org/class/Citation> .\n')
            g.write(f'<http://ma-graph.org/entity/{PaperId}-{PaperReferenceId}> <http://purl.org/spar/cito/hasCitingEntity> <http://ma-graph.org/entity/{PaperId}> .\n')
            g.write(f'<http://ma-graph.org/entity/{PaperId}-{PaperReferenceId}> <http://purl.org/spar/cito/hasCitedEntity> <http://ma-graph.org/entity/{PaperReferenceId}> .\n')
            g.write(f'<http://ma-graph.org/entity/{PaperId}-{PaperReferenceId}> <http://purl.org/spar/c4o/hasContext> "{CitationContext}"^^<http://www.w3.org/2001/XMLSchema#string> .\n')