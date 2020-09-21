#!/bin/bash
python 00.prepare_paper_references.py
python 01.extract_paper_id_with_doi.py
python 02.extract_author_with_paper_id.py

sort -n -t$'\t' -k1 02.author_id_with_paper_id.txt > 02.author_id_with_paper_id_sorted.txt

python 03.extract_paper_with_author_id.py

sort -n -t$'\t' -k1 03.paper_id_with_author_id.txt > 03.paper_id_with_author_id_sorted.txt 

python 04.author_id_merge_paper_id.py
python 05.paper_id_merge_author_ids.py
python 06.add_to_authors_paper_id.py
python 07.add_to_authors_doi.py
python 08.add_to_authors_coauthors.py
python 09.add_to_authors_titles.py
python 10.add_to_authors_year.py
python 11.add_to_authors_journal_and_conference.py
python 12.add_to_authors_references.py

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

python 13.disambiguation_data.py
python 14.recreate_files