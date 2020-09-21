with open("/pfs/work7/workspace/scratch/utdkf-ws_lin-0/0.data/0.mag_20200619/advanced/EntityRelatedEntities.txt", "r") as f:
    with open("12.EntityRelatedEntities.nt", "w") as g:
        for line in f:
            EntityId = line.split("\t")[0]
            RelatedEntityId = line.split("\t")[2]
            g.write(f'<http://ma-graph.org/entity/{EntityId}> <http://ma-graph.org/property/isRelatedTo> <http://ma-graph.org/entity/{RelatedEntityId}> .\n')
            