dict_of_years = {}
line_count = 1

print("Starting...")

#Add path to Papers.txt
with open("Papers.txt", "r") as inp:
    for line in inp:
        print("Loading: " + str(line_count))

        paper_id = line.split("\t")[0].strip()
        year = line.split("\t")[7].strip()
        dict_of_years[paper_id] = year

        line_count += 1

line_count = 1

with open("09.authors_with_titles.txt", "r") as inp:
    with open("10.authors_with_year.txt", "w") as outp:
        for line in inp:
            print("Searching: " + str(line_count))

            paper_ids = line.split("\t")[9].strip().split(",")
            years = set()
            for paper_id in paper_ids:
                try:
                    years.add(dict_of_years[paper_id])
                except KeyError:
                    pass
            outp.write(line.strip("\n") + "\t" + ",".join(years) + "\n")

            line_count += 1

print("Finished.")

