with open("/pfs/work7/workspace/scratch/utdkf-ws_lin-0/0.data/0.mag_20200619/mag/ConferenceInstances.txt", "r") as f:
    with open("03.ConferenceInstances.nt", "w") as g:
        for line in f:
            ConferenceInstanceId, NormalizedName, DisplayName, ConferenceSeriesId, Location, OfficialUrl, StartDate, EndDate, AbstractRegistrationDate, SubmissionDeadlineDate, NotificationDueDate, FinalVersionDueDate, PageCount, PaperFamilyCount, CitationCount, Latitude, Longitude, CreatedDate  = line.strip("\n").split("\t")
            g.write(f'<http://ma-graph.org/entity/{ConferenceInstanceId}> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ma-graph.org/class/ConferenceInstance> .\n')
            if not DisplayName == "":
                g.write(f'<http://ma-graph.org/entity/{ConferenceInstanceId}> <http://xmlns.com/foaf/0.1/name> "{DisplayName}"^^<http://www.w3.org/2001/XMLSchema#string> .\n')
            if not ConferenceInstanceId == "":
                g.write(f'<http://ma-graph.org/entity/{ConferenceInstanceId}> <http://purl.org/dc/terms/isPartOf> <http://ma-graph.org/entity/{ConferenceSeriesId}> .\n')
            if not Location == "":
                g.write(f'<http://ma-graph.org/entity/{ConferenceInstanceId}> <dbpedia.org/ontology/location> <{Location}> .\n')
            if not OfficialUrl == "":
                g.write(f'<http://ma-graph.org/entity/{ConferenceInstanceId}> <http://xmlns.com/foaf/0.1/homepage> <{OfficialUrl}> .\n')
            if not StartDate == "":
                g.write(f'<http://ma-graph.org/entity/{ConferenceInstanceId}> <http://purl.org/NET/c4dm/timeline.owl#start> "{StartDate}"^^<http://www.w3.org/2001/XMLSchema#date> .\n')
            if not EndDate == "":
                g.write(f'<http://ma-graph.org/entity/{ConferenceInstanceId}> <http://purl.org/NET/c4dm/timeline.owl#end> "{EndDate}"^^<http://www.w3.org/2001/XMLSchema#date> .\n')
            if not AbstractRegistrationDate == "":
                g.write(f'<http://ma-graph.org/entity/{ConferenceInstanceId}> <http://ma-graph.org/property/abstractRegistrationDate> "{AbstractRegistrationDate}"^^<http://www.w3.org/2001/XMLSchema#date> .\n')
            if not SubmissionDeadlineDate == "":
                g.write(f'<http://ma-graph.org/entity/{ConferenceInstanceId}> <http://ma-graph.org/property/submissionDeadlineDate> "{SubmissionDeadlineDate}"^^<http://www.w3.org/2001/XMLSchema#date> .\n')
            if not NotificationDueDate == "":
                g.write(f'<http://ma-graph.org/entity/{ConferenceInstanceId}> <http://ma-graph.org/property/notificationDueDate> "{NotificationDueDate}"^^<http://www.w3.org/2001/XMLSchema#date> .\n')
            if not FinalVersionDueDate == "":
                g.write(f'<http://ma-graph.org/entity/{ConferenceInstanceId}> <http://ma-graph.org/property/finalVersionDueDate> "{FinalVersionDueDate}"^^<http://www.w3.org/2001/XMLSchema#date> .\n')
            if not PageCount == "":
                g.write(f'<http://ma-graph.org/entity/{ConferenceInstanceId}> <http://ma-graph.org/property/pageCount> "{PageCount}"^^<http://www.w3.org/2001/XMLSchema#integer> .\n')
            if not PaperFamilyCount == "":
                g.write(f'<http://ma-graph.org/entity/{ConferenceInstanceId}> <http://ma-graph.org/property/paperFamilyCount> "{PaperFamilyCount}"^^<http://www.w3.org/2001/XMLSchema#integer> .\n')
            if not CitationCount == "":
                g.write(f'<http://ma-graph.org/entity/{ConferenceInstanceId}> <http://ma-graph.org/property/citationCount> "{CitationCount}"^^<http://www.w3.org/2001/XMLSchema#integer> .\n')
            if not CreatedDate == "":
                g.write(f'<http://ma-graph.org/entity/{ConferenceInstanceId}> <http://purl.org/dc/terms/created> "{CreatedDate}"^^<http://www.w3.org/2001/XMLSchema#date> .\n')

