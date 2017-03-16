import requests
import datetime
from bs4 import BeautifulSoup
import json
import csv

today = str(datetime.datetime.now().date())

# Create a list of dictionaries for JSON Object
response = []

# Scrape APNewsBriefs with requests
urlSDNewsBriefs = 'https://slickdeals.net/'
pageSDNewsBriefs = requests.get(urlSDNewsBriefs)

# Prepare for parsing APNewsBriefs with BeautifulSoup
soupSDNewsBriefs = BeautifulSoup(pageSDNewsBriefs.content, 'lxml')

# Parse SDNewsBriefs url
# 'position' marks the beginning of each news brief in the html
# All other data is found in its relationship to 'position'

#for position in soupSDNewsBriefs.find_all('div' , class_='fpGridBox grid frontpage cat'):
for position in soupSDNewsBriefs.find_all('div' , class_='fpItem '):
    itemName = position.find('a', class_='itemTitle').string
    if(position.find('div' , class_='itemPrice') is not None):
        price = position.find('div' , class_='itemPrice').next_element.split('\n')[0]
    if (position.find('div', class_='priceInfo') is not None and price + position.find('div', class_='priceInfo').string is not None and position.find('div' , class_='itemPrice').string is not None):
        extraInfo = position.find('div', class_='priceInfo').string

    link = 'https://slickdeals.net' + position.find('a', class_='itemTitle').get('href')
    retailer = position.find('a' , class_='itemStore').string.split('\u00a0')[0]

    # Make changes to response for APNewsBriefs
    response.append({'Item': itemName, 'Price': price, 'Extra Info' : extraInfo, 'Retailer' : retailer, 'Source': link})

for position in soupSDNewsBriefs.find_all('div' , class_='fpItem pctOff '):
    itemName = position.find('a', class_='itemTitle').string
    if(position.find('div' , class_='itemPrice') is not None):
        price = position.find('div' , class_='itemPrice').next_element.split('\n')[0]
    if (position.find('div', class_='priceInfo') is not None and price + position.find('div', class_='priceInfo').string is not None and position.find('div' , class_='itemPrice').string is not None):
        extraInfo = position.find('div', class_='priceInfo').string

    link = 'https://slickdeals.net' + position.find('a', class_='itemTitle').get('href')
    retailer = position.find('a' , class_='itemStore').string.split('\u00a0')[0]

    # Make changes to response for APNewsBriefs
    response.append({'Item': itemName, 'Price': price, 'Extra Info' : extraInfo, 'Retailer' : retailer, 'Source': link})


# Write response to JSON file
postingsFile = '/Users/Danny/Desktop/CSC3130/WebProject_dannyyq/' + today + '.SDNewsBriefs.json'

#Write response to JSON file in another location
#postingsFile = '/SDBriefs/' + today + '.SDNewsBriefs.json'

with open(postingsFile, 'w') as outfile:
    json.dump(response, outfile, sort_keys=True, indent=2)

outfile.close()
