import statistics

with open("00.entity_resolution/05.paper_id_with_merged_author_id.txt", "r") as f:
    paper_dict = {}
    for line in f:
        paperid = line.split("\t")[0]
        authors = len(line.strip().split("\t")[1].split(","))
        paper_dict[paperid] = authors


#Add file path for Papers.txt
with open("Papers.txt", "r") as f:
    year_dict = {year: [] for year in range(1800, 2022)}
    for line in f:
        paperid = line.split("\t")[0]
        year = line.split("\t")[7]
        if not year == "":
            try:
                year_dict[int(year)].append(paper_dict[paperid])
            except KeyError:
                pass

with open("10.author_number_by_year.txt", "w") as f:
    for item in year_dict:
        f.write(f"{item}\t{statistics.mean(year_dict[item])}\t{max(year_dict[item])}\n")
