import requests
#import csv
from bs4 import BeautifulSoup as bs
#import pandas as pd

URLi = "https://spb.postupi.online/vuzi/?page_num=" #_blocks of universities
universities = []
try:
	PAGES = int(input("Enter the amount of pages ypu need to parse: "))
except ValueError:
	PAGES = 4

def getBlocksText(URL): #_get blocks of information about each university
	soup = bs(requests.get(URL).text, 'html.parser')
	blocks = soup.find_all('div', class_='list__info')
	
	for block in blocks:
		universities.append(
			{
				'Университет': block.find('h2', class_='list__h').get_text(strip=True),
				'Ссылка на бакалавриат': block.find('div', class_='dropdown-menu btn-ddown__menu').find('a').get('href'),
				'Средний балл ЕГЭ (бюджет)': block.find('span', class_='list__score-sm').find('b').get_text(strip=True),
			}
		)

def byPages(pages=4):
	for i in range(pages):
		URL = URLi + str(i+1)
		print(i+1, 'page', URL)
		getBlocksText(URL)

byPages(PAGES)

print(universities)
