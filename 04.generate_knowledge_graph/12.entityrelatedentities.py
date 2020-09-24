with open("EntityRelatedEntities.txt", "r") as f:
    with open("12.EntityRelatedEntities.nt", "w") as g:
        for line in f:
            EntityId = line.split("\t")[0]
            RelatedEntityId = line.split("\t")[2]
            g.write(f'<http://ma-graph.org/entity/{EntityId}> <http://ma-graph.org/property/isRelatedTo> <http://ma-graph.org/entity/{RelatedEntityId}> .\n')
            