# enhancing_the_makg
Code for the Master Thesis "Enhancing the Microsoft Academic Knowledge Graph"

<b>Entity Resolution</b>

Required Packages:
[pyjarowinkler](https://pypi.org/project/pyjarowinkler/)

Data preperation + disambiguation + recreating file format: 00.execute.sh executes files 00-14 with required sorting in between

Edit the following data paths for MAG files:  
* 00.prepare_paper_references.py: path to PaperReferences.txt  
* 01.extract_paper_id_with_doi.py: path to Papers.txt  
* 02.extract_author_with_paper_id.py: path to PaperAuthorAffiliations.txt  
* 03.extract_paper_with_author_id.py: path to PaperAuthorAffiliations.txt  
* 06.add_to_authors_paper_id.py: path to Authors.txt  
* 09.add_to_authors_titles.py: path to Papers.txt  
* 10.add_to_authors_year.py: path to Papers.txt  
* 11.add_to_authors_journal_and_conference.py: path to Papers.txt  
* 14.recreate_files.py: path to PaperAuthorAffiliations.txt  

Files 15-19 are used for evaluation in the Thesis


<b>Field of Study Classification</b>

Required Packages:
[NLTK]

* files 00 and 01 are used to convert MAG paper abstracts from Inverted Indexes to Full Texts  
* file 02 is used to extract field of study labels from the MAG (all 19 low level FoS), edit the path to FieldsOfStudy.txt accordingly  
* execute both 04 files in sequence to generate the data set using indirect labels  
files require a sorted version of the PaperFieldsOfStudy.txt file, which can be done with the following code:
````
mkdir sort
split -l 5000000 -d 12.authors_with_references.txt sort/sort_file
cd sort
for file in sort_file*; do
    echo $file
    LANG=en_US.UTF-8 LC_ALL=C sort -t$'\t' -k3 -o $file $file
    done
LANG=en_US.UTF-8 LC_ALL=C sort -t$'\t' -k3 sort_file* > ../12.authors_with_references_sorted.txt
cd ..
rm -r sort
````
