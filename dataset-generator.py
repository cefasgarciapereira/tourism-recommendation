import json
import requests
import csv

VENUE_EXPLORE = 'https://api.foursquare.com/v2/venues/explore/'
CLIENT_ID = 'ALCBWJD2IZ40YSYPYNMZAAKUXGOYCKSZQVRGHWXUXVC0GAFR'
CLIEND_SECRET = 'NYX4JFVQ4JO1FPR2G2SVQLJORNQOHJGIJ05MIRWPIVX3LN50'
VERSION = '20180323'
NEAR = 'pocos de caldas'
LIMIT = 1000000
venuesId = []
usersId = []
users_line = []
matrix = [['IGNORE']]
ALL_CATEGORIES = ('4eb1d4d54b900d56c88a45fc,'#mountain
                  '4bf58dd8d48988d164941735,'#square
                  '4bf58dd8d48988d159941735,'#trail
                  '4bf58dd8d48988d12d941735,'#monument
                  '4bf58dd8d48988d163941735,'#park
                  '5267e4d9e4b0ec79466e48d1,'#musical_festival
                  '4bf58dd8d48988d137941735,'#thatre
                  '4bf58dd8d48988d11b941735,'#pub
                  '4bf58dd8d48988d181941735')#museum

def getVenuesID():
    print('Getting venues ids')
    params = dict(
      client_id = CLIENT_ID,
      client_secret = CLIEND_SECRET,
      v = VERSION,
      near = NEAR,
      categoryId= ALL_CATEGORIES,
      limit = LIMIT
    )

    resp = requests.get(url=VENUE_EXPLORE, params=params).json()
    venues = resp['response']['groups'][0]['items']
    i = 0
    for venue in venues:
      venuesId.append(venue['venue']['id'])
      matrix[0].append(venue['venue']['id'])
      i = i+1
    return

def getVenuesLikes(venueId,col):
    VENUE_DETAILS = 'https://api.foursquare.com/v2/venues/'+venueId+'/likes'
    params = dict(
      client_id = CLIENT_ID,
      client_secret = CLIEND_SECRET,
      v = VERSION,
      limit= LIMIT
    )

    resp = requests.get(url=VENUE_DETAILS, params=params).json()

    print(resp['response']['likes']['items'])
    users = resp['response']['likes']['items']

    for user in users:
        for i in range(0,len(matrix)):
            if(matrix[i][0] == user['id']):
                matrix[i][col] = '1'
                continue

    row = []
    for user in users:
        row.append(user['id'])
        for i in range(1, len(matrix[0])):
            if(i == col):
                row.append('1')
            else:
                row.append('')
        matrix.append(row)
        row = []
    return

def writeCSV():
    print('Writing csv')
    with open('dataset.csv','w') as f:
        thewriter = csv.writer(f)
        venues = ['IGNORE']
        for venueId in venuesId:
            venues.append(venueId)

        thewriter.writerow(matrix[0])
        for i in range(1,len(matrix)):
            thewriter.writerow(matrix[i])
    return

getVenuesID()

print('Getting venues likes')
getVenuesLikes('4c518ecb3940be9ac8600c09',0)
# for i in range(0, len(venuesId)):
#     getVenuesLikes(venuesId[i],i)

#writeCSV()
print('Done!')
