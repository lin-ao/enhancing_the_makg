import os
import xml.etree.ElementTree as ET

#Add directory to ORCID files
directory = "ORCID_files"

print("Starting...")

with open("15.orcid_title_doi.txt", "w") as outp:
    for folder in os.listdir(directory):
        print(folder)
        
        folder_path = os.path.join(directory, folder)
        if os.path.isdir(folder_path):
            for subfolder in os.listdir(folder_path):
                subfolder_path = os.path.join(folder_path, subfolder)
                for subsubfolder in os.listdir(subfolder_path):
                    subsubfolder_path = os.path.join(subfolder_path, subsubfolder)
                    orcid = subsubfolder_path.split("/")[-1]

                    real_name = ""
                    educations_path = os.path.join(subsubfolder_path, "educations")
                    employments_path = os.path.join(subsubfolder_path, "employments")
                    works_path = os.path.join(subsubfolder_path, "works")

                    try:
                        for education_file in os.listdir(educations_path):
                            education_file_path = os.path.join(educations_path, education_file)
                            tree = ET.parse(education_file_path)
                            root = tree.getroot()
                            name = root.find("{http://www.orcid.org/ns/common}source")
                            if name is not None:
                                name2 = name.find("{http://www.orcid.org/ns/common}source-name")
                            if name2 is not None:
                                real_name = name2.text

                    except OSError:
                        try:
                            for employment_file in os.listdir(employments_path):
                                    employments_file_path = os.path.join(employments_path, employment_file)
                                    tree = ET.parse(employments_file_path)
                                    root = tree.getroot()
                                    name = root.find("{http://www.orcid.org/ns/common}source")
                                    if name is not None:
                                        name2 = name.find("{http://www.orcid.org/ns/common}source-name")
                                    if name2 is not None:
                                        real_name = name2.text
                        except OSError:
                            pass
                    
                    try:
                        for work_file in os.listdir(works_path):
                            work_file_path = os.path.join(works_path, work_file)
                            tree = ET.parse(work_file_path)
                            root = tree.getroot()

                            title = root.find("{http://www.orcid.org/ns/work}title")
                            if title is not None:
                                real_title = title.find("{http://www.orcid.org/ns/common}title").text.replace("\t", " ").replace("\\", " ")
                            
                            real_doi = ""
                            doi = root.find("{http://www.orcid.org/ns/common}external-ids")
                            if doi is not None:
                                dois = doi.findall("{http://www.orcid.org/ns/common}external-id")
                                for doi in dois:
                                    if doi.find("{http://www.orcid.org/ns/common}external-id-type").text == "doi":
                                        real_doi = doi.find("{http://www.orcid.org/ns/common}external-id-value").text   

                        outp.write("\t".join([orcid, real_name, real_title, real_doi]) + "\n") 

                    except OSError:
                        pass
                                 
print("Finished.")