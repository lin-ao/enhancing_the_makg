year_dict = {}

#Add file path to Papers.txt
with open("Papers.txt", "r") as inp:
    for line in inp:
        year = line.split("\t")[7]
        try:
            year_dict[year] += 1
        except KeyError:
            year_dict[year] = 1
with open("01.paper_year_distribution.txt", "w") as outp:
    for item in year_dict:
        outp.write(f"{item}\t{year_dict[item]}\n")
