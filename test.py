import json
from app import Hero

import requests

url = 'https://stzb.cbg.163.com/cgi/api/get_equip_detail'

data = {
    'serverid' : '1',
    'ordersn': '202403190302116-1-4AVAGRTDJSEYJ9'
}

response = requests.post(url, data=data)
account_data = json.loads(response.text)['equip']
del account_data['equip_desc']

print(account_data)
# hero_data = json.loads(account_data)['card']

# for hero in hero_data:
#     print(Hero(**hero).display_info())







