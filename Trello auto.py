import requests, json
from config import *

key = '####################'
token = '##############################################'

card_id_dic = {
'Junta aerodinámica': '5f3aa462f922ee3b9837a8e2',
'Junta transmisión': '5f3aa4d1bcfb7e4d44a08f58',
'Junta general': '5f3ad0d2410816268428fcf1'
}

card_enpoint = 'https://api.trello.com/1/cards/{}'.format(card_id_dic.get('Junta general'))
headers = {"Accept": "application/json"}
querry = {
'key': key,
'token': token
}

def add_card(url, querry):
    r = requests.request(
    "POST",
    url,
    params = querry
    )
    print(r.text)

#Algoritmo

pastDue = get_pastdue(card_enpoint, querry, headers)

remove_characters = pastDue[8:10]
newvalues = int(pastDue[8:10]) + 8

newDue = renew_card(remove_characters, pastDue, newvalues)

def get_pastdue(url, querry, headers):
    r = requests.request(
    "GET",
    url,
    headers = headers,
    params = querry
    )
    return json.loads(r.text).get('due')

def renew_card(remove, past, new):
    for character in remove:
        pastDue = pastDue.replace(character, str(new))
        print(pastDue)
        return pastDue
