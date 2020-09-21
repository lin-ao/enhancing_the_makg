with open("/pfs/work7/workspace/scratch/utdkf-ws_lin-0/0.data/0.mag_20200619/advanced/FieldOfStudyChildren.txt", "r") as f:
    with open("13.FieldOfStudyChildren.nt", "w") as g:
        for line in f:
            FieldOfStudyId = line.split("\t")[0]
            ChildFieldOfStudyId = line.split("\t")[1].strip()
            g.write(f'<http://ma-graph.org/entity/{ChildFieldOfStudyId}> <http://ma-graph.org/property/hasParent> <http://ma-graph.org/entity/{FieldOfStudyId}> .\n')
            