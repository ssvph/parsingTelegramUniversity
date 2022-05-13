import requests
#import csv
from bs4 import BeautifulSoup as bs
#import pandas as pd

"""
# Подключение к сайту
url_template = "https://spb.postupi.online/specialnosti/bakalavr/"
r = requests.get(url_template)
print(r.status_code)
soup = bs(r.text, 'html.parser')
#print(r.text)

# result_list['href'].append('https://www.work.ua'+name.a['href'])
# База итогового результата
#result_list = {'Направление': [], 'Идентификатор': [], 'Специальность': [], 'Проходной балл': [], 'Предметы ЕГЭ': [], }

#specialty_by_number = soup.find_all('', class_= '')

# Получение направления обучения [9:] и идентификатор [1:9]
number = soup.find_all('p', class_= 'list__pre')
for num in number:
	str0 = num.get_text()
	print('Направление --', str0[8:])
	print('Идентификатор --', str0[0:8])

# Получение специальности
specialty = soup.find_all('h2', class_= 'list__h')
for spe in specialty:
	#result_list['Специальность'].append(spe.a.get_text())
	print('Специальность --', spe.a.get_text())
"""

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
