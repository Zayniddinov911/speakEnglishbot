import requests

app_id = "7fc569dd"
app_key = "3222675d8c64f58afe92c39fd91b5fb4"
language = "en-gb"

def getDefinitions(word_id):
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    res = r.json()
    if 'error' in res.keys():
        return False

    output = {}
    senses = res['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
    definitions = []
    for sense in senses:
        definitions.append(f"* {sense['definitions'][0]}")
    output['definitions'] = "\n".join(definitions)

    return output

if __name__ == '__main__':
    print(getDefinitions('Great Britain'))
    print(getDefinitions('fdd'))
    