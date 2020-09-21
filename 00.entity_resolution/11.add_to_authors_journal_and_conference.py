dict_of_journals = {}
dict_of_conferences = {}
line_count = 1

print("Starting...")
print("Loading lists...")
#Add path to Papers.txt
with open("Papers.txt", "r") as inp:
    for line in inp:
        print("Loading: " + str(line_count))

        paper_id = line.split("\t")[0].strip()
        journal = line.split("\t")[11].strip()
        conference = line.split("\t")[12].strip()
        dict_of_journals[paper_id] = journal
        dict_of_conferences[paper_id] = conference

        line_count += 1

line_count = 1

with open("10.authors_with_year.txt", "r") as inp:
    with open("11.authors_with_journal_and_conference.txt", "w") as outp:
        for line in inp:
            print("Searching: " + str(line_count))

            paper_ids = line.split("\t")[9].strip().split(",")
            journals = set()
            conferences = set()
            for paper_id in paper_ids:
                try:
                    journals.add(dict_of_journals[paper_id])
                except KeyError:
                    pass
                try:
                    conferences.add(dict_of_journals[paper_id])
                except KeyError:
                    pass
            outp.write(line.strip("\n") + "\t" + ",".join(journals).strip(",") + "\t" + ",".join(conferences).strip(",") + "\n")

            line_count += 1

print("Finished.")
