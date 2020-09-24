with open("01.field_of_study_classification/10.paperid_with_fos.txt", "r") as f:
    with open("22.PaperFieldsOfStudyNew.nt", "w") as g:
        for line in f:
            PaperId, FieldOfStudy = line.strip("\n").split("\t")
            g.write(f'<http://ma-graph.org/entity/{PaperId}> <http://purl.org/spar/fabio/hasDiscipline> <http://ma-graph.org/entity/{FieldOfStudy}> .\n')