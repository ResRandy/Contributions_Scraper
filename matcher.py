from pykml import parser
import pymupdf

doc = pymupdf.open("Articles/113_seahorse_JB.pdf")
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

print(zoo_list)
# Parse the article txt and search for matches with every zoo name from leon
file_name = "output.txt"
with open(file_name, 'r', encoding='utf8') as file:
    article = file.read().replace('\n', '').replace("-", "")

    for zoo in zoo_list:
        if zoo in article:
            print(zoo)
