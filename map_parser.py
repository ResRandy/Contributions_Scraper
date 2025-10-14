from pykml import parser
import numpy as np

kml_file = "./leonmap.kml"

# Opens kml file from map website
with open(kml_file, encoding="utf8") as f:
    doc = parser.parse(f).getroot().Document

# Append every placemark name under Zoos and Aquariums
names = []
for pm in doc.Folder[4].Placemark:
    name = pm.name
    names.append(name)

sorted_names = np.array(names, dtype=object)           # or dtype='<U' if all are simple strings
sorted_arr = np.sort(sorted_names, kind='quicksort')     # 'quicksort' | 'mergesort' | 'heapsort' | 'stable'
sorted_list = list(sorted_arr)
# Write all names to a text file
with open('zoo_aquarium_list.txt', 'w', encoding="utf8") as f:
    for n in names:
        f.write(str(n) + '\n')
    f.close()

with open('zoo_aquarium_list_sorted.txt', 'w', encoding="utf8") as f:
    for n in sorted_list:
        f.write(str(n) + '\n')
    f.close()