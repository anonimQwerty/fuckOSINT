import requests, libs.logo, libs.users_agents

sites=['https://instagram.com/', 'https://twitter.com/', 'https://steamcommunity.com/id/', 'https://ok.ru/', 'https://www.youtube.com/user/', 'https://freelance.ru/', 'https://t.me/', 'https://github.com/', 
'https://gitlab.com/', 'https://habr.com/ru/users/', 'https://picsart.com/', 'https://www.youtube.com/c/', 'https://qiwi.me/', 'https://www.donationalerts.com/r/', 
'https://www.donationalerts.com/c/', 'https://vk.com/', "https://my.mail.ru/mail/", "https://www.drive2.ru/users/",  "https://4pda.ru/forum/index.php?act=search&source=pst&noform=1&username=", "https://forums.adobe.com/people/",
"https://ask.fm/", "https://badoo.com/profile/", "https://badoo.com/profile/", "https://www.bandcamp.com/", "https://bitcoinforum.com/profile/", "https://www.ebay.com/usr/", "https://www.reddit.com/user/", 
"https://steamcommunity.com/groups/", "https://tamtam.chat/", "https://www.tiktok.com/@", "https://www.twitch.tv/", "https://www.wikipedia.org/wiki/User:", "https://yandex.ru/collections/user/", "https://pikabu.ru/@", "https://zen.yandex.ru/",
 "https://www.facebook.com/public/"]

def check(header, target, proxy=0, use_proxy='n'):
	for i in sites:
		try:
			if use_proxy=='n':
				g=requests.get(i+target, headers=header)
			elif use_proxy=='y':
				g=requests.get(i+target, headers=header, proxy=proxy)
			
			if g.status_code==200:
				print(f'found {i+target}')
			else:
				print(f'{i} not found')
		except:
			print(f"Возможно сайт не доступен в вашем регионе {i}")

def main():
	libs.logo.logo()
	header=libs.users_agents.initHeaders()
	target=input('target: ')
	use_proxy=input("Use proxy (y/n)").lower()
	if use_proxy=='n':
		proxy=0
	elif use_proxy=='y':
		proxy=input('Input http proxy with port ')
		proxy={'http':'http://'+proxy,
		'https':'https://'+proxy}
	check(header, target, proxy, use_proxy)
	
if __name__ == '__main__':
	main()
