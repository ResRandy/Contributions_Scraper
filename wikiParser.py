import os

# Function is finds <a </a> which is the icon on the wiki page that indicates an entry and then afterwards just grabs


def parse_for_location(text):
    names = []
    _, crntPnt = entry(text, '<ul>', '<li>')
    
    if crntPnt == -1:
        return  "error with reading for lists (wikiParser, parse_for_location)"  # or handle the "not found" case before entering the loop
    
    while crntPnt > 0:

        # below will grab between 2 points inside of an html list item
        setText, crntPnt = entry(text[crntPnt:],'::marker',', \"')
        names = names.append(setText)
        
        names[names.len() - 1], _ = entry(names[names.len() - 1],'\"',',') if setText.find('<a') == -1 else entry(names[names.len() - 1],'> ','<')

  
    with open('zoo_aquarium_list.txt', 'w', encoding="utf8") as f:
        for n in names:
            f.write(str(n) + '\n')



# this function extracts text between two markers and was created mostly by gpt-4
def entry(text,m1,m2):
    start_idx = text.find(m1)
    end_idx = text.find(m2, start_idx + len(m1))
    
    if start_idx == -1 or end_idx == -1:
        return None, -1  # Symbols not found
    
    return text[start_idx + len(m1):end_idx], end_idx + 1