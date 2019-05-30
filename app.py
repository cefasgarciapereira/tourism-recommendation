import json
import requests

url = 'https://api.foursquare.com/v2/venues/explore'

art_fun = '4d4b7104d754a06370d81259'
museum = '4bf58dd8d48988d181941735'
pub = '4bf58dd8d48988d11b941735'
theatre = '4bf58dd8d48988d137941735'
musical_festival = '5267e4d9e4b0ec79466e48d1'
park = '4bf58dd8d48988d163941735'
monument = '4bf58dd8d48988d12d941735'
trail = '4bf58dd8d48988d159941735'
square =  '4bf58dd8d48988d164941735'
mountain = '4eb1d4d54b900d56c88a45fc'

all_categories = ('4eb1d4d54b900d56c88a45fc,'#mountain
                  '4bf58dd8d48988d164941735,'#square
                  '4bf58dd8d48988d159941735,'#trail
                  '4bf58dd8d48988d12d941735,'#monument
                  '4bf58dd8d48988d163941735,'#park
                  '5267e4d9e4b0ec79466e48d1,'#musical_festival
                  '4bf58dd8d48988d137941735,'#thatre
                  '4bf58dd8d48988d11b941735,'#pub
                  '4bf58dd8d48988d181941735')#museum

params = dict(
  client_id='ALCBWJD2IZ40YSYPYNMZAAKUXGOYCKSZQVRGHWXUXVC0GAFR',
  client_secret='NYX4JFVQ4JO1FPR2G2SVQLJORNQOHJGIJ05MIRWPIVX3LN50',
  v='20190529',
  near='pocos de caldas',
  categoryId= all_categories,
  limit=900
)

resp = requests.get(url=url, params=params).json()
venues = resp['response']['groups'][0]['items']

for venue in venues:
  print(venue['venue']['id'] +": "+venue['venue']['name'])
#data = json.loads(resp.text)

#data = data['response']['groups']

# ,Place1,Place2 ,Place3
# User1,5,3,1
# User2,4,5,?
# User3,4,2,2
# User4,1,?,4