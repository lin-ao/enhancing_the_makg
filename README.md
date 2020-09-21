# enhancing_the_makg
Code for the Master Thesis "Enhancing the Microsoft Academic Knowledge Graph"

<b>Entity Resolution</b>

Required Packages:
[pyjarowinkler](https://pypi.org/project/pyjarowinkler/)


All in one script: 00.execute.sh executes files 00-14 with required sorting in between

Edit the following data paths for MAG files:

*00.prepare_paper_references.py: path to PaperReferences.txt

*01.extract_paper_id_with_doi.py: path to Papers.txt

*02.extract_author_with_paper_id.py: path to PaperAuthorAffiliations.txt

*03.extract_paper_with_author_id.py: path to PaperAuthorAffiliations.txt

*06.add_to_authors_paper_id.py: path to Authors.txt

*09.add_to_authors_titles.py: path to Papers.txt

*10.add_to_authors_year.py: path to Papers.txt

*11.add_to_authors_journal_and_conference.py: path to Papers.txt

*14.recreate_files.py: path to PaperAuthorAffiliations.txt
