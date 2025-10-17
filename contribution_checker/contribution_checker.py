import os
import re

def search_in_text():
    file_path = input("Enter the file path for a text file (e.g. example.txt): ")
    list_path = "zoo_aquarium_list.txt"
    file_name = os.path.basename(file_path)

    # read the main text
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read().lower()

    # read the zoo/aquarium list
    aquarium_zoo_list = []
    with open(list_path, "r", encoding="utf-8") as x:
        for line in x:
            line = line.strip()
            if line:
                aquarium_zoo_list.append(line.lower())  

    # find contributions from aquarium/zoo list to given text file
    contributions = []
    for phrase in aquarium_zoo_list:
        p = phrase.strip().lower()
        if not p:
            continue
        # whole-phrase match
        if re.search(r'(?<!\w)'+re.escape(p)+r'(?!\w)', text):
            contributions.append(phrase)

    contributions = list(dict.fromkeys(contributions))

    seahorse_mentions = text.count("seahorse") + text.count("seahorses")
    print("Contributions found:", contributions if contributions else "None")
    print("File Name:", file_name)
    print("Seahorse Mentions:", seahorse_mentions)

search_in_text()