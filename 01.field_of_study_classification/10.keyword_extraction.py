import spacy
import pytextrank
import multiprocessing
import sys

filename = sys.argv[1]
nlp = spacy.load("en_core_web_sm")
tr = pytextrank.TextRank()
nlp.add_pipe(tr.PipelineComponent, name="textrank", last=True)

def extraction(item):
    output = ""
    paperid = item[0]
    text = item[1]
    doc = nlp(text)
    for p in doc._.phrases[:5]:
        output += f"{paperid}\t{p.rank:.4f}\t{p.count:5d}\t{p.text}\n"
    return output
   
line_count = 1
with open(f"00.paper_abstracts.txt", "r") as f:
    abstracts = []
    for line in f:
        print("Loading: " + str(line_count))
        paperid = line.strip().split("\t")[0]
        text = line.strip().replace(paperid, "").replace("\t", " ")
        abstracts.append((paperid, text))
        line_count += 1

with open(f"10.paper_keywords.txt", "w") as f:
    p = multiprocessing.Pool(8)
    for result in p.imap(extraction, abstracts):
        f.write(result)

