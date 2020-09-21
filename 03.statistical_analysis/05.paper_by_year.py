def by_year(input_file):    
    year_dict = {}
    with open(f"{input_file}.txt", "r") as inp:
        for line in inp:
            year = line.split("\t")[7]
            try:
                year_dict[year] += 1
            except KeyError:
                year_dict[year] = 1
    with open(f"{input_file}_output.txt", "w") as outp:
        for item in year_dict:
            outp.write(f"{item}\t{year_dict[item]}\n")

by_year(121332964)
by_year(138885662)
by_year(144133560)
by_year(17744445)
by_year(205649164)
by_year(41008148)
by_year(95457728)
by_year(127313418)
by_year(142362112)
by_year(15744967)
by_year(185592680)
by_year(33923547)
by_year(71924100)
by_year(127413603)
by_year(144024400)
by_year(162324750)
by_year(192562407)
by_year(39432304)
by_year(86803240)
