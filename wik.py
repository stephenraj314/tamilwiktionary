import requests
import json
import unicodedata
S = requests.Session()

query = input("Enter the word to search : ")

URL = "https://ta.wiktionary.org/w/api.php"
PARAMS = {
    "action": "query",
    "prop": "revisions",
    "titles": query,
    "rvprop": "content",
    "formatversion":"2",
    "format": "json",
}

response = S.get(url=URL, params=PARAMS)

print(response)
data = response.json()
#print(json.dumps(data, indent=2))
unicodestring=data['query']['pages'][0]['revisions'][0]['content']

print(unicodedata.normalize('NFC', unicodestring))

