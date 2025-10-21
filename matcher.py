import pymupdf
import os

def findContributions(files):
    ending = ""
    for f in files:
        doc = pymupdf.open(f)
        out = open("output.txt", "wb") # create a text output
        for page in doc: # iterate the document pages
            text = page.get_text().encode("utf8") # get plain text (is in UTF-8)
            out.write(text) # write text of page
            out.write(bytes((12,))) # write page delimiter (form feed 0x0C)
        out.close()

        zoo_list = []

        # Transform the zoo list from leon's world to an array of names
        with open("zoo_aquarium_list.txt", 'r', encoding='utf8') as zoos:
            zoo_list = zoos.readlines()
            zoo_list = [zoo.replace("\n", "") for zoo in zoo_list]

        # Parse the article txt and search for matches with every zoo name from leon
        file_name = "output.txt"
        with open(file_name, 'r', encoding='utf8') as file:

            # Joins every line of the article into one string, adds a space in between each line, removes all trailing whitepsace from each line, replaces all - with ""
            article = " ".join(line.rstrip() for line in file).replace("-", "")
            detected_zoos = []
            for zoo in zoo_list:
                if zoo in article:
                    detected_zoos.append(zoo)
            
            detected_seahorse = False
            if "Seahorse" or "seahorse" in article:
                detected_seahorse = True


            if detected_zoos:
                ending = f"\n {ending}\n{f}\n"
                for zoo in detected_zoos:
                    ending = (f"{ending} Zoo/Aquarium detected: {zoo}\n")
                if detected_seahorse:
                    ending = ending + "The word seahorse is mentioned in article"
        ending += "\n"

    return ending


def testMatcher():
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
            zoo_list = zoos.readlines()
            zoo_list = [zoo.replace("\n", "") for zoo in zoo_list]

        # Parse the article txt and search for matches with every zoo name from leon
        file_name = "output.txt"
        with open(file_name, 'r', encoding='utf8') as file:

            # Joins every line of the article into one string, adds a space in between each line, removes all trailing whitepsace from each line, replaces all - with ""
            article = " ".join(line.rstrip() for line in file).replace("-", "")
            detected_zoos = []
            for zoo in zoo_list:
                if zoo in article:
                    detected_zoos.append(zoo)
            
            detected_seahorse = False
            if "Seahorse" or "seahorse" in article:
                detected_seahorse = True


            if detected_zoos:
                print("\n" + f)
                for zoo in detected_zoos:
                    print(f"Zoo/Aquarium detected: {zoo}")
                if detected_seahorse:
                    print("The word seahorse is mentioned in article")