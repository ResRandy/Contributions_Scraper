from pykml import parser
import numpy as np


def remove_symbols_keep_letters(text, keep_spaces=True):
    """Return a copy of text with only Unicode letters kept.

    - Keeps characters where str.isalpha() is True (this includes accented letters).
    - If keep_spaces is True, whitespace characters are preserved so words stay separated.
    - If text is None, returns None.

    Examples:
        remove_symbols_keep_letters("St. John's Zoo 123!") -> "St Johns Zoo"
    """
    if text is None:
        return None
    s = str(text)
    # Build result by keeping alphabetic characters and (optionally) whitespace
    return ''.join(ch for ch in s if ch.isalpha() or (keep_spaces and ch.isspace()))

kml_file = "./leonmap.kml"

# Opens kml file from map website
with open(kml_file, encoding="utf8") as f:
    doc = parser.parse(f).getroot().Document

# Append every placemark name under Zoos and Aquariums
names = []
for pm in doc.Folder[4].Placemark:
    name = pm.name
    names.append(name)
print(type(names))

sorted_names = np.array(names, dtype=object)           # or dtype='<U' if all are simple strings
sorted_arr = np.sort(sorted_names, kind='quicksort')     # 'quicksort' | 'mergesort' | 'heapsort' | 'stable'
sorted_list = list(sorted_arr)
# Write all names to a text file
with open('zoo_aquarium_list.txt', 'w', encoding="utf8") as f:
    for n in names:
        f.write(str(n) + '\n')
    f.close()


# Create a cleaned version keeping only letters (and spaces) and write to a separate file
cleaned_list = [remove_symbols_keep_letters(n, keep_spaces=True) for n in sorted_list]
with open('zoo_aquarium_list_letters_only.txt', 'w', encoding="utf8") as f:
    for n in cleaned_list:
        f.write(str(n) + '\n')
    f.close()

