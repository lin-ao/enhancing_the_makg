with open("Journals.txt", "r") as f:
    with open("05.Journals.nt", "w") as g:
        for line in f:
            JournalId, Rank, NormalizedName, DisplayName, Issn, Publisher, Webpage, PaperCount, PaperFamilyCount, CitationCount, CreatedDate = line.strip("\n").split("\t")
            g.write(f'<http://ma-graph.org/entity/{JournalId}> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ma-graph.org/class/ConferenceSeries> .\n')
            if not Rank == "":
                g.write(f'<http://ma-graph.org/entity/{JournalId}> <http://ma-graph.org/property/rank> "{Rank}"^^<http://www.w3.org/2001/XMLSchema#integer> .\n')
            if not DisplayName == "":
                g.write(f'<http://ma-graph.org/entity/{JournalId}> <http://xmlns.com/foaf/0.1/name> "{DisplayName}"^^<http://www.w3.org/2001/XMLSchema#string> .\n')
            if not Issn == "":
                g.write(f'<http://ma-graph.org/entity/{JournalId}> <http://id.loc.gov/vocabulary/identifiers/issn> "{Issn}"^^<http://www.w3.org/2001/XMLSchema#string> .\n')
            if not Publisher == "":
                g.write(f'<http://ma-graph.org/entity/{JournalId}> <http://purl.org/dc/terms/publisher> "{Publisher}"^^<http://www.w3.org/2001/XMLSchema#string> .\n')
            if not Webpage == "":
                g.write(f'<http://ma-graph.org/entity/{JournalId}> <http://xmlns.com/foaf/0.1/homepage> "{Webpage}"^^<http://www.w3.org/2001/XMLSchema#string> .\n')
            if not PaperCount == "":
                g.write(f'<http://ma-graph.org/entity/{JournalId}> <http://ma-graph.org/property/paperCount> "{PaperCount}"^^<http://www.w3.org/2001/XMLSchema#integer> .\n')
            if not PaperFamilyCount == "":
                g.write(f'<http://ma-graph.org/entity/{JournalId}> <http://ma-graph.org/property/paperFamilyCount> "{PaperFamilyCount}"^^<http://www.w3.org/2001/XMLSchema#integer> .\n')
            if not CitationCount == "":
                g.write(f'<http://ma-graph.org/entity/{JournalId}> <http://ma-graph.org/property/citationCount> "{CitationCount}"^^<http://www.w3.org/2001/XMLSchema#integer> .\n')
            if not CreatedDate == "":    
                g.write(f'<http://ma-graph.org/entity/{JournalId}> <http://purl.org/dc/terms/created> "{CreatedDate}"^^<http://www.w3.org/2001/XMLSchema#date> .\n')