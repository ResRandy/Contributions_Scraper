import pymupdf
import os
import re

def findContributions(files):
    ending = "" # Initialize an empty string to store results


    for f in files:
        doc = pymupdf.open(f)
        out = open("output.txt", "wb") # create a text output
        for page in doc: # iterate the document pages
            text = page.get_text().encode("utf8") # get plain text (is in UTF-8)
            out.write(text) # write text of page
            out.write(bytes((12,))) # write page delimiter (form feed 0x0C)
        out.close()

        #zoo_list = []

        # Transform the zoo list from leon's world to an array of names
        with open("zoo_aquarium_list.txt", 'r', encoding='utf8') as zoos:
            # normalize zoo names: lowercase, replace hyphens with spaces, collapse whitespace
            zoo_list = [re.sub(r"\s+", " ", z.strip().lower().replace("-", " ")).strip() for z in zoos]

        # Parse the article txt and search for matches with every zoo name from leon
        file_name = "output.txt"
        with open(file_name, 'r', encoding='utf8') as file:

            # Join lines, fix hyphenation and normalize punctuation/whitespace
            article = " ".join(line.rstrip() for line in file)
            # remove hyphen-newline artifacts from line breaks (word splits)
            article = article.replace("-\n", "")
            # replace remaining hyphens with spaces so names like 'Sea-Life' -> 'sea life'
            article = article.replace("-", " ")
            article = re.sub(r"\s+", " ", article).lower()
            
            detected_zoos = []
            for zoo in zoo_list:
                if zoo in article:
                    detected_zoos.append(zoo)
            
            # only keep most specific zoo matches so that Ex: 
            # 'oceanarium' is not reported if 'oceanarium of xyz' is found
            pruned = []
            for z in detected_zoos:
                if not any(z != other and z in other for other in detected_zoos):
                    if z not in pruned:
                        pruned.append(z)
            detected_zoos = pruned

            # only look for whole word matches of 'seahorse' or 'seahorses'
            matches = re.findall(r"\bseahorses?\b", article)
            seahorse_mentions = len(matches)
            detected_seahorse = seahorse_mentions > 0
            
            #if detected_seahorse:
            #    print("The word seahorse is mentioned in article", seahorse_mentions, "times")
            #else:
            #    print("The word seahorse is not mentioned in article")               
                
        ending += "File Name: " + os.path.basename(f) + "\n"
        if detected_zoos:
            for zoo in detected_zoos:
                ending += f"Zoo/Aquarium detected: {zoo}\n"
        else:
            ending += "No Zoo/Aquarium detected\n"

        if detected_seahorse:
            ending += f"Seahorses mentioned {seahorse_mentions} times\n"
        else:
            ending += "Seahorses not mentioned\n"

        ending += "\n"

    return ending




def main():
    files = [f for f in os.listdir("Articles") if os.path.isfile(os.path.join("Articles", f))]

    TESTING_ARTICLE = "Articles/Aquatic Conservation - 2012 - Caldwell - Revisiting two sympatric European seahorse species  apparent decline in the.pdf"

    for f in files:
        doc = pymupdf.open("Articles/" + f)
        out = open("output.txt", "wb") # create a text output
        for page in doc: # iterate the document pages
            text = page.get_text().encode("utf8") # get plain text (is in UTF-8)
            out.write(text) # write text of page
            out.write(bytes((12,))) # write page delimiter (form feed 0x0C)
        out.close()

        zoo_list = []

        # Transform the zoo list from leon's world to an array of names
        with open("zoo_aquarium_list.txt", 'r', encoding='utf8') as zoos:
            zoo_list = [re.sub(r"\s+", " ", z.strip().lower().replace("-", " ")).strip() for z in zoos]

        # Parse the article txt and search for matches with every zoo name from leon
        file_name = "output.txt"
        with open(file_name, 'r', encoding='utf8') as file:
            article = " ".join(line.rstrip() for line in file)
            article = article.replace("-\n", "")
            article = article.replace("-", " ")
            article = re.sub(r"\s+", " ", article)
            
            detected_zoos = []
            for zoo in zoo_list:
                if zoo in article:
                    detected_zoos.append(zoo)
            

            pruned = []
            for z in detected_zoos:
                if not any(z != other and z in other for other in detected_zoos):
                    if z not in pruned:
                        pruned.append(z)
            detected_zoos = pruned

         
            matches = re.findall(r"\bseahorses?\b", article)
            seahorse_mentions = len(matches)
            detected_seahorse = seahorse_mentions > 0
            
            
            
            #if "seahorse" in article or "seahorses" in article:
            #    detected_seahorse = True
            #    seahorse_mentions = article.count("seahorse") + article.count("seahorses")
                #if detected_seahorse:
                #    print("The word seahorse is mentioned in article", seahorse_mentions, " times")
                #else: 
                #    print("The word seahorse is not mentioned in article")                


        print("\n" + f)

        if detected_zoos:
            for zoo in detected_zoos:
                print(f"Zoo/Aquarium detected: {zoo}")
        else:
            print("No Zoo/Aquarium detected in", f)

        if detected_seahorse:
            print(f"Seahorses mentioned {seahorse_mentions} times")
        else:
            print("Seahorses not mentioned")

                
