with open("/pfs/work7/workspace/scratch/utdkf-ws_lin-0/0.data/0.mag_20200619/mag/Papers.txt", "r") as f:
    with open("10.Papers.nt", "w") as g:
        for line in f:
            PaperId, Rank, Doi, DocType, PaperTitle, OriginalTitle, BookTitle, Year, Date, OnlineDate, Publisher, JournalId, ConferenceSeriesId, ConferenceInstanceId, Volume, Issue, FirstPage, LastPage, ReferenceCount, CitationCount, EstimatedCitation, OriginalVenue, FamilyId, CreatedDate = line.strip("\n").split("\t")
            if DocType == "Journal":
                g.write(f'<http://ma-graph.org/entity/{PaperId}> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ma-graph.org/class/Paper> .\n')
            elif DocType == "Conference":
                g.write(f'<http://ma-graph.org/entity/{PaperId}> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://purl.org/spar/fabio/ConferencePaper> .\n')
            elif DocType == "Book":
                g.write(f'<http://ma-graph.org/entity/{PaperId}> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://purl.org/spar/fabio/Book> .\n')
            elif DocType == "BookChapter":
                g.write(f'<http://ma-graph.org/entity/{PaperId}> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://purl.org/spar/fabio/BookChapter> .\n')
            elif DocType == "Patent":
                g.write(f'<http://ma-graph.org/entity/{PaperId}> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://purl.org/spar/fabio/PatentDocument> .\n')
            
            if not Rank == "":
                g.write(f'<http://ma-graph.org/entity/{PaperId}> <http://ma-graph.org/property/rank> "{Rank}"^^<http://www.w3.org/2001/XMLSchema#integer> .\n')
            if not Doi == "":
                g.write(f'<http://ma-graph.org/entity/{PaperId}> <http://purl.org/spar/datacite/doi> "{Doi}"^^<http://www.w3.org/2001/XMLSchema#string> .\n')
            if not OriginalTitle == "":
                g.write(f'<http://ma-graph.org/entity/{PaperId}> <http://purl.org/dc/terms/title> "{OriginalTitle}"^^<http://www.w3.org/2001/XMLSchema#string> .\n')
            if not BookTitle == "":
                g.write(f'<http://ma-graph.org/entity/{PaperId}> <http://purl.org/dc/terms/title> "{BookTitle}"^^<http://www.w3.org/2001/XMLSchema#string> .\n')
            if not Date == "":
                g.write(f'<http://ma-graph.org/entity/{PaperId}> <http://prismstandard.org/namespaces/basic/2.0/publicationDate> "{Date}"^^<http://www.w3.org/2001/XMLSchema#date> .\n')
            if not Publisher == "":
                g.write(f'<http://ma-graph.org/entity/{PaperId}> <http://purl.org/dc/terms/publisher> "{Publisher}"^^<http://www.w3.org/2001/XMLSchema#string> .\n')
            if not JournalId == "":
                g.write(f'<http://ma-graph.org/entity/{PaperId}> <http://ma-graph.org/property/appearsInJournal> "<http://ma-graph.org/entity/{JournalId}> .\n')
            if not ConferenceSeriesId == "":
                g.write(f'<http://ma-graph.org/entity/{PaperId}> <http://ma-graph.org/property/appearsInConferenceSeries> "<http://ma-graph.org/entity/{ConferenceSeriesId}> .\n')
            if not ConferenceInstanceId == "":
                g.write(f'<http://ma-graph.org/entity/{PaperId}> <http://ma-graph.org/property/appearsInConferenceInstance> "<http://ma-graph.org/entity/{ConferenceInstanceId}> .\n')
            if not Volume == "":
                g.write(f'<http://ma-graph.org/entity/{PaperId}> <http://prismstandard.org/namespaces/basic/2.0/volume> "{Volume}"^^<http://www.w3.org/2001/XMLSchema#integer> .\n')
            if not Issue == "":
                g.write(f'<http://ma-graph.org/entity/{PaperId}> <http://prismstandard.org/namespaces/basic/2.0/issueIdentifier> "{Issue}"^^<http://www.w3.org/2001/XMLSchema#string> .\n')
            if not FirstPage == "":
                g.write(f'<http://ma-graph.org/entity/{PaperId}> <http://prismstandard.org/namespaces/basic/2.0/startingPage> "{FirstPage}"^^<http://www.w3.org/2001/XMLSchema#integer> .\n')
            if not LastPage == "":
                g.write(f'<http://ma-graph.org/entity/{PaperId}> <http://prismstandard.org/namespaces/basic/2.0/endingPage> "{LastPage}"^^<http://www.w3.org/2001/XMLSchema#integer> .\n')
            if not ReferenceCount == "":
                g.write(f'<http://ma-graph.org/entity/{PaperId}> <http://ma-graph.org/property/referenceCount> "{ReferenceCount}"^^<http://www.w3.org/2001/XMLSchema#integer> .\n')
            if not CitationCount == "":
                g.write(f'<http://ma-graph.org/entity/{PaperId}> <http://ma-graph.org/property/citationCount> "{CitationCount}"^^<http://www.w3.org/2001/XMLSchema#integer> .\n')
            if not EstimatedCitation == "":
                g.write(f'<http://ma-graph.org/entity/{PaperId}> <http://ma-graph.org/property/estimatedCitationCount> "{EstimatedCitation}"^^<http://www.w3.org/2001/XMLSchema#integer> .\n')
            if not FamilyId == "":
                g.write(f'<http://ma-graph.org/entity/{PaperId}> <http://ma-graph.org/property/familyId> "{FamilyId}"^^<http://www.w3.org/2001/XMLSchema#integer> .\n')
            if not CreatedDate == "":    
                g.write(f'<http://ma-graph.org/entity/{PaperId}> <http://purl.org/dc/terms/created> "{CreatedDate}"^^<http://www.w3.org/2001/XMLSchema#date> .\n')