import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 
import string

nltk.download('stopwords')
nltk.download('punkt')

stop_words = set(stopwords.words('english'))

line_count = 1

with open("00.paper_abstracts.txt", "r") as inp:
    with open("01.tokenized_abstracts.txt", "w") as outp:
        for line in inp:
            print(line_count)
            abstract = line.split("\t")[1].strip()
            temp_abstract = abstract.translate(str.maketrans('', '', string.punctuation))
            word_tokens = word_tokenize(temp_abstract) 
            ps = PorterStemmer()
            tokenized_abstract = [ps.stem(w) for w in word_tokens if not w in stop_words]
            outp.write(line.split("\t")[0] + "\t" + " ".join(tokenized_abstract) + "\n")
            line_count += 1
