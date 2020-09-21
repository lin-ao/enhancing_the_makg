years_dict = {}
for year in range(1800, 2022):
    years_dict[year] = set()

with open("00.entity_resolution/10.authors_with_year.txt", "r") as f:
    for line in f:
        authorid = line.split("\t")[0]
        years = line.split("\t")[-1].strip()
        if not years == "":
            f1 = lambda x: x
            f2 = lambda x: max(x-1, 1800)
            f3 = lambda x: min(x+1, 2021)
            years_list = list(map(int, years.split(",")))
            active_years = [f(year) for year in years_list for f in (f1, f2, f3)]
            for year in active_years:
                years_dict[year].add(authorid)
with open("08.author_activity.txt", "w") as f:
    for item in years_dict:
        f.write(f"{item}\t{len(years_dict[item])}\n")
