import statistics

with open("00.entity_resolution/05.paper_id_with_merged_author_id.txt", "r") as f:
    author_count = [len(line.strip().split("\t")[1].split(",")) for line in f]
with open("00.entity_resolution/04.author_id_with_merged_paper_id.txt", "r") as f:
    paper_count = [len(line.strip().split("\t")[1].split(",")) for line in f]
with open("00.entity_resolution/08.authors_with_co_authors.txt", "r") as f:
    coauthor_count = [len(line.strip("\n").split("\t")[11].split(",")) for line in f]    
    
with open("02.author_paper_average.txt", "w") as f:
    f.write(f"Average author per paper: {statistics.mean(author_count)}\n")
    f.write(f"Maximum author per paper: {max(author_count)}\n")
    f.write(f"Average paper per author: {statistics.mean(paper_count)}\n")
    f.write(f"Maximum paper per author: {max(paper_count)}\n")
    f.write(f"Average coauthor per author: {statistics.mean(coauthor_count)}\n")
    f.write(f"Maximum coauthor per author: {max(coauthor_count)}\n")
