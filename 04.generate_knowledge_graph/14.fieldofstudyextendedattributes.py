with open("/pfs/work7/workspace/scratch/utdkf-ws_lin-0/0.data/0.mag_20200619/advanced/FieldOfStudyExtendedAttributes.txt", "r") as f:
    with open("14.FieldOfStudyExtendedAttributes.nt", "w") as g:
        for line in f:
            FieldOfStudyId, AttributeType, AttributeValue = line.strip("\n").split("\t")
            g.write(f'<http://ma-graph.org/entity/{FieldOfStudyId}> <http://ma-graph.org/property/hasAttributeType> "{AttributeType}"^^<http://www.w3.org/2001/XMLSchema#integer> .\n')
            g.write(f'<http://ma-graph.org/entity/{FieldOfStudyId}> <http://ma-graph.org/property/hasAttributeValue"> "{AttributeValue}"^^<http://www.w3.org/2001/XMLSchema#string> .\n')