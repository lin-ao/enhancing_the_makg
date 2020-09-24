with open("ConferenceSeries.txt", "r") as f:
    with open("04.ConferenceSeries.nt", "w") as g:
        for line in f:
            ConferenceSeriesId, Rank, NormalizedName, DisplayName, PaperCount, PaperFamilyCount, CitationCount, CreatedDate = line.strip("\n").split("\t")
            g.write(f'<http://ma-graph.org/entity/{ConferenceSeriesId}> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ma-graph.org/class/ConferenceSeries> .\n')
            if not Rank == "":
                g.write(f'<http://ma-graph.org/entity/{ConferenceSeriesId}> <http://ma-graph.org/property/rank> "{Rank}"^^<http://www.w3.org/2001/XMLSchema#integer> .\n')
            if not DisplayName == "":
                g.write(f'<http://ma-graph.org/entity/{ConferenceSeriesId}> <http://xmlns.com/foaf/0.1/name> "{DisplayName}"^^<http://www.w3.org/2001/XMLSchema#string> .\n')
            if not PaperCount == "":
                g.write(f'<http://ma-graph.org/entity/{ConferenceSeriesId}> <http://ma-graph.org/property/paperCount> "{PaperCount}"^^<http://www.w3.org/2001/XMLSchema#integer> .\n')
            if not PaperFamilyCount == "":
                g.write(f'<http://ma-graph.org/entity/{ConferenceSeriesId}> <http://ma-graph.org/property/paperFamilyCount> "{PaperFamilyCount}"^^<http://www.w3.org/2001/XMLSchema#integer> .\n')
            if not CitationCount == "":
                g.write(f'<http://ma-graph.org/entity/{ConferenceSeriesId}> <http://ma-graph.org/property/citationCount> "{CitationCount}"^^<http://www.w3.org/2001/XMLSchema#integer> .\n')
            if not CreatedDate == "":    
                g.write(f'<http://ma-graph.org/entity/{ConferenceSeriesId}> <http://purl.org/dc/terms/created> "{CreatedDate}"^^<http://www.w3.org/2001/XMLSchema#date> .\n')