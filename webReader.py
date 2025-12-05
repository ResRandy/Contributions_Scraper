import requests
from wikiParser import parse_for_location

def grab_wiki_data(url):
    try:

        Response = requests.get(url)
        
        
        if Response.status_code == 200:
            htmlAsText = Response.text

            locations = parse_for_location(htmlAsText)


        else:
            print("There was an error fetching the Wikipedia page (no 200).")

    except Exception as e:
        print(f"Error fetching Wikipedia page: {e}")
        return None
    
    return locations


url = "https://en.wikipedia.org/wiki/List_of_zoos_in_the_United_States"



try:

    zoosResponse = requests.get(url)
    
    
    if zoosResponse.status_code == 200:
        zooHtmlAsText = zoosResponse.text

        zoos = parse_for_location(zooHtmlAsText)


    else:
        print("There was an error fetching the Zoos Wikipedia page (no 200).")

except Exception as e:
    print(f"Error fetching Wikipedia page: {e}")

url = "https://en.wikipedia.org/wiki/List_of_aquaria_by_country"

try:

    aqsResponse = requests.get(url)
    
    
    if aqsResponse.status_code == 200:
        aqsHtmlAsText = aqsResponse.text

        aqs = parse_for_location(aqsHtmlAsText)


    else:
        print("There was an error fetching the Zoos Wikipedia page (no 200).")

except Exception as e:
    print(f"Error fetching Wikipedia page: {e}")


if zoos.exists() and aqs.exists():
    response = zoos + "\n\n" + aqs
