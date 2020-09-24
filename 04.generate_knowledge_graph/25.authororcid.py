with open("00.entity_resolution/18.authors_with_orcid.txt", "r") as f:
    with open("25.AuthorORCID.nt", "w") as g:
        for line in f:
            AuthorId = line.split("\t")[0]
            ORCID = line.split("\t")[17]
            g.write(f'<http://ma-graph.org/entity/{AuthorId}> <http://ma-graph.org/property/hasORCID> <{ORCID}>^^<http://www.w3.org/2001/XMLSchema#string> .\n')
            