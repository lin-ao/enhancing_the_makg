import statistics

paper_references = {}
paper_citations = {}
#Add file path for Papers.txt
with open("Papers.txt", "r") as f:
    for line in f:
        year = line.split("\t")[7]
        references = int(line.split("\t")[18])
        citations = int(line.split("\t")[19])
        if not year == "":
            try:
                paper_references[year].append(references)
            except KeyError:
                paper_references[year] = [references]
            try:
                paper_citations[year].append(citations)
            except KeyError:
                paper_citations[year] = [citations]

with open("07.paper_references_by_year.txt", "w") as f:
    for item in paper_references:
        f.write(f"{item}\t{sum(paper_references[item])}\t{len(paper_references[item])}\t{statistics.mean(paper_references[item])}\t{statistics.median(paper_references[item])}\t{max(paper_references[item])}\n")

with open("07.paper_citations_by_year.txt", "w") as f:
    for item in paper_citations:
        f.write(f"{item}\t{sum(paper_citations[item])}\t{len(paper_citations[item])}\t{statistics.mean(paper_citations[item])}\t{statistics.median(paper_citations[item])}\t{max(paper_citations[item])}\n")
