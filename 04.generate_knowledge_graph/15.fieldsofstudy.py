with open("FieldsOfStudy.txt", "r") as f:
    with open("15.FieldsOfStudy.nt", "w") as g:
        for line in f:
            FieldsOfStudyId, Rank, NormalizedName, DisplayName, MainType, Level, PaperCount, PaperFamilyCount, CitationCount, CreateDate = line.strip("\n").split("\t")
            g.write(f'<http://ma-graph.org/entity/{FieldsOfStudyId}> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ma-graph.org/class/FieldOfStudy> .\n')
            if not Rank == "":
                g.write(f'<http://ma-graph.org/entity/{FieldsOfStudyId}> <http://ma-graph.org/property/rank> "{Rank}"^^<http://www.w3.org/2001/XMLSchema#integer> .\n')
            if not DisplayName == "":
                g.write(f'<http://ma-graph.org/entity/{FieldsOfStudyId}> <http://xmlns.com/foaf/0.1/name> "{DisplayName}"^^<http://www.w3.org/2001/XMLSchema#string> .\n')
            if not Level == "":
                g.write(f'<http://ma-graph.org/entity/{FieldsOfStudyId}> <http://ma-graph.org/property/level> "{Level}"^^<http://www.w3.org/2001/XMLSchema#integer> .\n')
            if not PaperCount == "":
                g.write(f'<http://ma-graph.org/entity/{FieldsOfStudyId}> <http://ma-graph.org/property/paperCount> "{PaperCount}"^^<http://www.w3.org/2001/XMLSchema#integer> .\n')
            if not PaperFamilyCount == "":
                g.write(f'<http://ma-graph.org/entity/{FieldsOfStudyId}> <http://ma-graph.org/property/paperFamilyCount> "{PaperFamilyCount}"^^<http://www.w3.org/2001/XMLSchema#integer> .\n')
            if not CitationCount == "":
                g.write(f'<http://ma-graph.org/entity/{FieldsOfStudyId}> <http://ma-graph.org/property/citationCount> "{CitationCount}"^^<http://www.w3.org/2001/XMLSchema#integer> .\n')
            if not CreateDate == "":
                g.write(f'<http://ma-graph.org/entity/{FieldsOfStudyId}> <http://purl.org/dc/terms/created> "{CreateDate}"^^<http://www.w3.org/2001/XMLSchema#date> .\n')