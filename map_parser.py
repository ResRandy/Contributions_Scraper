from pykml import parser

kml_file = "./leonmap.kml"

# Opens kml file from map website
with open(kml_file, encoding="utf8") as f:
    doc = parser.parse(f).getroot().Document

# Append every placemark name under Zoos and Aquariums
names = []
for pm in doc.Folder[4].Placemark:
    name = pm.name
    names.append(name)

# Write all names to a text file
with open('zoo_aquarium_list.txt', 'w', encoding="utf8") as f:
    for n in names:
        f.write(str(n) + '\n')
