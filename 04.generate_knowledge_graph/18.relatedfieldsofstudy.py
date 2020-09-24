with open("RelatedFieldOfStudy.txt", "r") as f:
    with open("18.RelatedFieldOfStudy.nt", "w") as g:
        for line in f:
            FieldOfStudy1, Type1, FieldOfStudy2, Type2, Rank = line.strip("\n").split("\t")
            g.write(f'<http://ma-graph.org/entity/{FieldOfStudy1}> <http://ma-graph.org/property/isRelatedTo> <http://ma-graph.org/entity/{FieldOfStudy2}> .\n')
            if Type1 == "disease":
                if Type2 == "disease_cause":
                    g.write(f'<http://ma-graph.org/entity/{FieldOfStudy1}> <http://ma-graph.org/property/diseaseHasDiseaseCause> <http://ma-graph.org/entity/{FieldOfStudy2}> .\n')
                if Type2 == "medical_treatment":
                    g.write(f'<http://ma-graph.org/entity/{FieldOfStudy1}> <http://ma-graph.org/property/diseaseHasMedicalTreatment> <http://ma-graph.org/entity/{FieldOfStudy2}> .\n')
                if Type2 == "symptom":
                    g.write(f'<http://ma-graph.org/entity/{FieldOfStudy1}> <http://ma-graph.org/property/diseaseHasSymptom> <http://ma-graph.org/entity/{FieldOfStudy2}> .\n')
            elif Type1 =="medical_treatment":
                if Type2 == "disease_cause":
                    g.write(f'<http://ma-graph.org/entity/{FieldOfStudy1}> <http://ma-graph.org/property/medicalTreatmentForDiseaseCause> <http://ma-graph.org/entity/{FieldOfStudy2}> .\n')
                if Type2 == "symptom":
                    g.write(f'<http://ma-graph.org/entity/{FieldOfStudy1}> <http://ma-graph.org/property/medicalTreatmentForSymptom> <http://ma-graph.org/entity/{FieldOfStudy2}> .\n')
            elif Type1 =="symptom":
                if Type2 == "disease_cause":
                    g.write(f'<http://ma-graph.org/entity/{FieldOfStudy1}> <http://ma-graph.org/property/symptomHasDiseaseCause> <http://ma-graph.org/entity/{FieldOfStudy2}> .\n')