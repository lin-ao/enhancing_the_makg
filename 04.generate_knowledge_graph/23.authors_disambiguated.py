with open("/pfs/work7/workspace/scratch/utdkf-ws_lin-0/mag/14.Authors_new.txt", "r") as f:
    with open("02.Authors.nt", "w") as g:
        for line in f:
            AuthorId, Rank, NormalizedName, DisplayName, LastKnownAffiliationId, PaperCount, PaperFamilyCount, CitationCount, CreateDate = line.strip("\n").split("\t")
            g.write(f'<http://ma-graph.org/entity/{AuthorId}> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ma-graph.org/class/Author> .\n')
            if not Rank == "":
                g.write(f'<http://ma-graph.org/entity/{AuthorId}> <http://ma-graph.org/property/rank> "{Rank}"^^<http://www.w3.org/2001/XMLSchema#integer> .\n')
            if not LastKnownAffiliationId == "":
                g.write(f'<http://ma-graph.org/entity/{AuthorId}> <http://www.w3.org/ns/org#memberOf> <http://ma-graph.org/entity/{LastKnownAffiliationId}> .\n')
            if not DisplayName == "":
                g.write(f'<http://ma-graph.org/entity/{AuthorId}> <http://xmlns.com/foaf/0.1/name> "{DisplayName}"^^<http://www.w3.org/2001/XMLSchema#string> .\n')
            if not PaperCount == "":
                g.write(f'<http://ma-graph.org/entity/{AuthorId}> <http://ma-graph.org/property/paperCount> "{PaperCount}"^^<http://www.w3.org/2001/XMLSchema#integer> .\n')
            if not PaperFamilyCount == "":
                g.write(f'<http://ma-graph.org/entity/{AuthorId}> <http://ma-graph.org/property/paperFamilyCount> "{PaperFamilyCount}"^^<http://www.w3.org/2001/XMLSchema#integer> .\n')
            if not CitationCount == "":
                g.write(f'<http://ma-graph.org/entity/{AuthorId}> <http://ma-graph.org/property/citationCount> "{CitationCount}"^^<http://www.w3.org/2001/XMLSchema#integer> .\n')
            if not CreateDate == "":
                g.write(f'<http://ma-graph.org/entity/{AuthorId}> <http://purl.org/dc/terms/created> "{CreateDate}"^^<http://www.w3.org/2001/XMLSchema#date> .\n')