import requests, json



def get_data():
    url = 'https://www.163hot.net/st/bulletin/getData'
    response = requests.get(url)
    data = json.loads(response.text)['data']
    teamData = data['teamData']
    return teamData


def print_data():
    team_data = get_data()
    for server_data in team_data:
        server_list = server_data['teamid'].split(";")
        for i in range(0, len(server_list)):
            print('\'' + server_list[i] + '\' : \'' + server_data['teamtype'] + "\'", end=', ')


def save_data():
    team_data = get_data()
    with open('data.json', 'w') as outfile:
        for server_data in team_data:
            server_list = server_data['teamid'].split(";")
            for i in range(0, len(server_list)):
                outfile.write(server_list[i] + "\n")


if __name__ == '__main__':
    mode = input('Enter Mode: ')
    if len(mode):
        save_data()
    else:
        print_data()


