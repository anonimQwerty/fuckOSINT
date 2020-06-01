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







def main():
	logo.logo()
	ip = input("target ip: ")
	print('Поиск информации по торентах. Ожидайте \n')
	torrent(ip)
	#print('')