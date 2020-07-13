import libs.logo as logo
import requests
from bs4 import BeautifulSoup






# Searching via torent
def torrent(target_ip):
	headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4086.0 Safari/537.36",
    "Connection": "keep-alive",
    "Host": "iknowwhatyoudownload.com",
    "Referer": "https://iknowwhatyoudownload.com"}
	page =requests.get("https://iknowwhatyoudownload.com/ru/peer/?ip=" + target_ip,
           headers=headers)
	soup = BeautifulSoup(page.content, "html.parser")
	table = soup.find(class_="table").find("tbody")
	torrents = table.find_all("tr")
	for torrent in torrents:
		first, last = torrent.find_all(class_="date-column")
		first, last = first.text, last.text
		category = torrent.find(class_="category-column").text
		name = torrent.find(class_="name-column").text.replace("\n", '').replace('    ', '')
		size = torrent.find(class_="size-column").text
		print(f'Использовано первый раз: {first}, использовано последний раз: {last}, тип торрента: {category}, название торенрта: {name}, размер торента: {size}\n')


def ip_info(ip):
	page =requests.get(f"http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query")
	page=page.json()
	if page['status']=='success':
		print(f'''
Континент: {page['continent']}
Страна: {page['country']}
Код страны: {page['countryCode']}
Регион: {page['region']}
Название региона: {page['regionName']}
Город: {page['city']}
Район: {page['district']}
Почтовый индекс: {page['zip']}
Широта: {page['lat']}
Долгота: {page['lon']}
Часовой пояс: {page['timezone']}
Часовой пояс UTC DST смещение в секундах: {page['offset']}
Национальная валюта: {page['currency']}
Имя провайдера: {page['isp']}
Имя организации: {page['org']}
AS номер и организация: {page['as']}
AS Имя: {page['asname']}
Обратный DNS IP: {page['reverse']}
Мобильное соединение: {page['mobile']}
Прокси, ВПН или принадлежность к сети ТОР: {page['proxy']}
Хостинг, или дата-центр: {page['hosting']}
IP использованый для запроса: {page['query']}
''')
	else:
		print('No success')


def main():
	logo.logo()
	ip = input("target ip: ")
	print('Поиск информации по торентах. Ожидайте \n')
	torrent(ip)
	print('нформация по IP')
	ip_info(ip)
	#print('')
