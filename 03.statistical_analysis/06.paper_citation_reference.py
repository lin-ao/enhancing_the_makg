import statistics

paper_references = []
paper_citations = []
#Add file path for Papers.txt
with open("Papers.txt", "r") as f:
    for line in f:
        references = int(line.split("\t")[18])
        citations = int(line.split("\t")[19])
        paper_references.append(references)
        paper_citations.append(citations)

paper_references_filtered = list(filter(lambda num: num != 0, paper_references))
paper_citations_filtered = list(filter(lambda num: num != 0, paper_citations))

with open("06.paper_references_citations_general.txt", "w") as f:
    f.write(f"Average number of references per paper: {statistics.mean(paper_references)}\n")
    f.write(f"Median number of references per paper: {statistics.median(paper_references_filtered)}\n")
    f.write(f"Maximum number of references per paper: {max(paper_references)}\n")
    f.write(f"Minimum number of references per paper: {min(paper_references)}\n")
    f.write(f"Paper with references: {len(paper_references_filtered)}\n")
    f.write(f"Average number of references per paper filtered: {statistics.mean(paper_references_filtered)}\n")
    f.write(f"Average number of citations per paper: {statistics.mean(paper_citations)}\n")
    f.write(f"Median number of citations per paper: {statistics.median(paper_citations_filtered)}\n")
    f.write(f"Maximum number of citations per paper: {max(paper_citations)}\n")
    f.write(f"Minimum number of citations per paper: {min(paper_citations)}\n")
    f.write(f"Paper with citations: {len(paper_citations_filtered)}\n")
    f.write(f"Average number of citations per paper filtered: {statistics.mean(paper_citations_filtered)}\n")

paper_references = {}
paper_citations = {}
#Add file path for Papers.txt
with open("Papers.txt", "r") as f:
    for line in f:
        papertype = line.split("\t")[3].lower()
        references = int(line.split("\t")[18])
        citations = int(line.split("\t")[19])
        try:
            paper_references[papertype].append(references)
            paper_citations[papertype].append(citations)
        except KeyError:
            paper_references[papertype] = [references]
            paper_citations[papertype] = [citations]

paper_references_filtered = {papertype: list(filter(lambda num: num != 0, paper_references[papertype])) for papertype in paper_references}
paper_citations_filtered = {papertype: list(filter(lambda num: num != 0, paper_citations[papertype])) for papertype in paper_citations}

with open("06.paper_references_citations_detailed.txt", "w") as f:
    for papertype in paper_references:
        f.write(f"Average number of references per paper {papertype}: {statistics.mean(paper_references[papertype])}\n")
        f.write(f"Median number of references per paper {papertype}: {statistics.median(paper_references_filtered[papertype])}\n")
        f.write(f"Maximum number of references per paper {papertype}: {max(paper_references[papertype])}\n")
        f.write(f"Minimum number of references per paper {papertype}: {min(paper_references[papertype])}\n")
        f.write(f"Paper with references {papertype}: {len(paper_references_filtered[papertype])}\n")
        f.write(f"Average number of references per paper filtered {papertype}: {statistics.mean(paper_references_filtered[papertype])}\n")
        f.write(f"Average number of citations per paper {papertype}: {statistics.mean(paper_citations[papertype])}\n")
        f.write(f"Median number of citations per paper {papertype}: {statistics.median(paper_citations_filtered[papertype])}\n")
        f.write(f"Maximum number of citations per paper {papertype}: {max(paper_citations[papertype])}\n")
        f.write(f"Minimum number of citations per paper {papertype}: {min(paper_citations[papertype])}\n")
        f.write(f"Paper with citations {papertype}: {len(paper_citations_filtered[papertype])}\n")
        f.write(f"Average number of citations per paper filtered {papertype}: {statistics.mean(paper_citations_filtered[papertype])}\n\n")
    
