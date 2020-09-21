with open("/pfs/work7/workspace/scratch/utdkf-ws_lin-0/3.field_of_study/3.mag_journal_labels/bert/0.data/paperid_with_fos.txt", "r") as f:
    fos_dict = {}
    for line in f:
        paperid = line.split("\t")[0]
        fos = line.split("\t")[1].strip()
        fos_dict[paperid] = fos

with open("/pfs/work7/workspace/scratch/utdkf-ws_lin-0/3.field_of_study/3.mag_journal_labels/00.labels.txt", "r") as f:
    labels = set()
    for line in f:
        labels.add(line.split("\t")[0])

for item in labels:
    f = open(f"04.field_of_study_over_time/{item}.txt", "w")
    f.close()

with open("/pfs/work7/workspace/scratch/utdkf-ws_lin-0/0.data/0.mag_20200619/mag/Papers.txt", "r") as f:
    for line in f:
        paperid = line.split("\t")[0]
        try:
            with open(f"04.field_of_study_over_time/{fos_dict[paperid]}.txt", "a") as g:
                g.write(line)
        except KeyError:
            pass
        

