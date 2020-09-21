with open("/pfs/work7/workspace/scratch/utdkf-ws_lin-0/3.field_of_study/3.mag_journal_labels/bert/0.data/paperid_with_fos.txt", "r") as f:
    with open("22.PaperFieldsOfStudyNew.nt", "w") as g:
        for line in f:
            PaperId, FieldOfStudy = line.strip("\n").split("\t")
            g.write(f'<http://ma-graph.org/entity/{PaperId}> <http://purl.org/spar/fabio/hasDiscipline> <http://ma-graph.org/entity/{FieldOfStudy}> .\n')