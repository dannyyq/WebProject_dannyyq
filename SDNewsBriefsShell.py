import requests
from bs4 import BeautifulSoup

# Scrape SDNewsBriefs with requests
urlSDNewsBriefs = 'https://slickdeals.net/'
pageSDNewsBriefs = requests.get(urlSDNewsBriefs)

# Prepare for parsing SDNewsBriefs with BeautifulSoup
soupSDNewsBriefs = BeautifulSoup(pageSDNewsBriefs.content, 'lxml')

#position = soupSDNewsBriefs.find('div' , class_='fpGridBox grid frontpage cat')
position = soupSDNewsBriefs.find('div' , class_='fpItem ')
itemName = position.find('a', class_= 'itemTitle').string
price = position.find('div', class_='itemPrice').string.split('\n')[0]
if (position.find('div', class_='priceInfo') is not None and price + position.find('div',class_='priceInfo').string is not None and position.find('div', class_='itemPrice').string is not None):
    price = price + ' (' + position.find('div', class_='priceInfo').string + ')'

retailer = position.find('a', class_='itemStore').string.split('\u00a0')[0]

link = 'https://slickdeals.net' + position.find('div', datahref_='').get('data-href')
#link = 'https://slickdeals.net' + position.find('a' , href_='').get('href')

print(itemName)
print(price)
print(retailer)
print(link)
