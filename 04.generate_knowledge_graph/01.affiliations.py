with open("Affiliations.txt", "r") as f:
    with open("01.Affiliations.nt", "w") as g:
        for line in f:
            AffiliationId, Rank, NormalizedName, DisplayName, GridId, OfficialPage, WikiPage, PaperCount, PaperFamilyCount, CitationCount, Latitude, Longitude, CreatedDate = line.strip("\n").split("\t")
            g.write(f'<http://ma-graph.org/entity/{AffiliationId}> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ma-graph.org//class/Affiliation> .\n')
            if not Rank == "":
                g.write(f'<http://ma-graph.org/entity/{AffiliationId}> <http://ma-graph.org/property/rank> "{Rank}"^^<http://www.w3.org/2001/XMLSchema#integer> .\n')
            if not DisplayName == "":
                g.write(f'<http://ma-graph.org/entity/{AffiliationId}> <http://xmlns.com/foaf/0.1/name> "{DisplayName}"^^<http://www.w3.org/2001/XMLSchema#string> .\n')
            if not GridId == "":
                g.write(f'<http://ma-graph.org/entity/{AffiliationId}> <http://ma-graph.org/property/grid> <http://www.grid.ac/institutes/{GridId}> .\n')
            if not OfficialPage == "":
                g.write(f'<http://ma-graph.org/entity/{AffiliationId}> <http://xmlns.com/foaf/0.1/homepage> <{OfficialPage}> .\n')
            if not WikiPage == "":
                g.write(f'<http://ma-graph.org/entity/{AffiliationId}> <http://www.w3.org/2000/01/rdf-schema#seeAlso> <{WikiPage}> .\n')
            if not WikiPage == "":
                g.write(f'<http://ma-graph.org/entity/{AffiliationId}> <http://www.w3.org/2002/07/owl#sameAs> <{WikiPage}> .\n')
            if not PaperCount == "":
                g.write(f'<http://ma-graph.org/entity/{AffiliationId}> <http://ma-graph.org/property/paperCount> "{PaperCount}"^^<http://www.w3.org/2001/XMLSchema#integer> .\n')
            if not PaperFamilyCount == "":
                g.write(f'<http://ma-graph.org/entity/{AffiliationId}> <http://ma-graph.org/property/paperFamilyCount> "{PaperFamilyCount}"^^<http://www.w3.org/2001/XMLSchema#integer> .\n')
            if not CitationCount == "":
                g.write(f'<http://ma-graph.org/entity/{AffiliationId}> <http://ma-graph.org/property/citationCount> "{CitationCount}"^^<http://www.w3.org/2001/XMLSchema#integer> .\n')
            if not Latitude == "":
                g.write(f'<http://ma-graph.org/entity/{AffiliationId}> <http://www.w3.org/2003/01/geo/wgs84_pos#lat> "{Latitude}"^^<http://www.w3.org/2001/XMLSchema#string> .\n')
            if not Longitude == "":
                g.write(f'<http://ma-graph.org/entity/{AffiliationId}> <http://www.w3.org/2003/01/geo/wgs84_pos#long> "{Longitude}"^^<http://www.w3.org/2001/XMLSchema#string> .\n')
            if not CreatedDate == "":
                g.write(f'<http://ma-graph.org/entity/{AffiliationId}> <http://purl.org/dc/terms/created> "{CreatedDate}"^^<http://www.w3.org/2001/XMLSchema#date> .')