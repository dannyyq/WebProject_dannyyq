import requests
from bs4 import BeautifulSoup

# Scrape SDNewsBriefs with requests
urlSDNewsBriefs = 'https://slickdeals.net/'
pageSDNewsBriefs = requests.get(urlSDNewsBriefs)

# Prepare for parsing SDNewsBriefs with BeautifulSoup
soupSDNewsBriefs = BeautifulSoup(pageSDNewsBriefs.content, 'lxml')

position = soupSDNewsBriefs.find('div' , class_='fpGridBox grid frontpage cat')
item = '' + position.find('a', class_='itemImageLink').get('title')
itemName = '' + position.find('a' , href_='').get('title')
price = position.find('div' , class_='itemPrice').string
link = 'https://slickdeals.net' + position.find('a' , href_='').get('href')

print(itemName)
print(price)
print(link)
