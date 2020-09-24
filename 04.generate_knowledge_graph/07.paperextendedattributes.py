with open("PaperExtendedAttributes.txt", "r") as f:
    with open("07.PaperExtendedAttributes.nt", "w") as g:
        for line in f:
            PaperId, AttributeType, AttributeValue = line.strip("\n").split("\t")
            if not AttributeType == "":
                g.write(f'<http://ma-graph.org/entity/{PaperId}> <http://ma-graph.org/property/hasAttributeType"> "{AttributeType}"^^<http://www.w3.org/2001/XMLSchema#integer> .\n')
            if not AttributeValue == "":
                g.write(f'<http://ma-graph.org/entity/{PaperId}> <http://ma-graph.org/property/hasAttributeValue"> "{AttributeValue}"^^<http://www.w3.org/2001/XMLSchema#string> .\n')
            