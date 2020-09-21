pred_list = ["<http://purl.org/dc/terms/title>", "<http://prismstandard.org/namespaces/1.2/basic/publicationDate>", "<http://purl.org/dc/terms/publisher>", "<http://ma-graph.org/property/referenceCount>", "<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>", "<http://ma-graph.org/property/appearsInConferenceSeries>", "<http://ma-graph.org/property/bookTitle>", "<http://ma-graph.org/property/citationCount>", "<http://ma-graph.org/property/appearsInConferenceInstance>", "<http://ma-graph.org/property/appearsInJournal>", "<http://ma-graph.org/property/paperCount>", "<http://xmlns.com/foaf/0.1/name>"]

with open("02.papers_input.txt", "w") as g:
    #Add file path to Papers.nt
    with open("Papers.nt", "r") as f:
        for line in f: 
            pred = line.split(" ")[1]
            if pred in pred_list:
                g.write(line)

    #Add file path to Journals.nt
    with open("Journals.nt", "r") as f:
       for line in f:
            pred = line.split(" ")[1]
            if pred in pred_list:
                g.write(line)

    #Add file path to ConferenceSeries.nt
    with open("ConferenceSeries.nt", "r") as f:
        for line in f:
            pred = line.split(" ")[1]
            if pred in pred_list:
                g.write(line)
        
