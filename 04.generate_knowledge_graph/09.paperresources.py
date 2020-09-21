with open("/pfs/work7/workspace/scratch/utdkf-ws_lin-0/0.data/0.mag_20200619/mag/PaperResources.txt", "r") as f:
    with open("09.PaperResources.nt", "w") as g:
        for line in f:
            PaperId, ResourceType, ResourceUrl, SourceUrl, RelationshipType = line.strip("\n").split("\t")
            if not ResourceType == "":
                g.write(f'<http://ma-graph.org/entity/{PaperId}> <http://ma-graph.org/property/rank> "{ResourceType}"^^<http://www.w3.org/2001/XMLSchema#integer> .\n')
            if not ResourceUrl == "":
                g.write(f'<http://ma-graph.org/entity/{PaperId}> <http://ma-graph.org/property/hasResourceUrl> "{ResourceUrl}"^^<http://www.w3.org/2001/XMLSchema#anyURI> .\n')
            if not RelationshipType == "":
                g.write(f'<http://ma-graph.org/entity/{PaperId}> <http://ma-graph.org/property/hasRelationshipType> "{RelationshipType}"^^<http://www.w3.org/2001/XMLSchema#integer> .\n')