import json

with open("00.paper_abstracts.txt", "w") as output:
    #Add path to PaperAbstractsInvertedIndex.txt.1
    with open("PaperAbstractsInvertedIndex.txt.1") as f:
        for line in f:
            paper_id, inverted_index = line.strip().split("\t")
            index_length = json.loads(inverted_index)["IndexLength"]
            indexes = json.loads(inverted_index)["InvertedIndex"]
            sentence_list = [" "]*index_length
            for word in indexes:
                word_index = list(indexes[word])
                for index in word_index:
                    sentence_list[index] = word.replace("\n", " ").replace("\r", "").replace("\t", " ")
            output.write(paper_id + "\t" + " ".join(sentence_list) + "\n")
    #Add path to PaperAbstractsInvertedIndex.txt.2        
    with open("PaperAbstractsInvertedIndex.txt.2") as f:
        for line in f:
            paper_id, inverted_index = line.strip().split("\t")
            index_length = json.loads(inverted_index)["IndexLength"]
            indexes = json.loads(inverted_index)["InvertedIndex"]
            sentence_list = [" "]*index_length
            for word in indexes:
                word_index = list(indexes[word])
                for index in word_index:
                    sentence_list[index] = word.replace("\n", " ").replace("\r", "").replace("\t", " ")
            output.write(paper_id + "\t" + " ".join(sentence_list) + "\n")
