import requests, json

url = 'https://www.163hot.net/st/bulletin/getData'

response = requests.get(url)

data = json.loads(response.text)['data']
teamData = data['teamData']
for serverData in teamData:
    serverText = serverData['teamid'].split(";")
    for i in range(0, len(serverText)):
        print('\'' + serverText[i] + '\' : \'' + serverData['teamtype'] + "\'", end=', ')

