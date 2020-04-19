import requests, os, random

headers_useragents=['Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3',
'Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)',
'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)',
'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1',
'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1',
'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)',
'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)',
'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)',
'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)',
'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)',
'Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)',
'Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51'
]

sites=['https://instagram.com/', 'https://twitter.com/', 'https://steamcommunity.com/id/', 'https://ok.ru/']
header_list=[]


def randomString(size):
	out_str = ''
	for i in range(0, size):
		a = random.randint(65, 90)
		out_str += chr(a)
	return(out_str)

def initHeaders():
	headers = {
				'User-Agent': random.choice(headers_useragents),
				'Cache-Control': 'no-cache',
				'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
				'Referer': 'http://www.google.com/?q=' + randomString(random.randint(5,10)),
				'Keep-Alive': str(random.randint(110,120)),
				'Connection': 'keep-alive'
				}

	return headers




def logo ():
	if os.name == 'nt':
		_ = os.system ('cls')
	else:
		_ = os.system ('clear')
	print('''

                            #######  #####  ### #     # ####### 
###### #    #  ####  #    # #     # #     #  #  ##    #    #    
#      #    # #    # #   #  #     # #        #  # #   #    #    
#####  #    # #      ####   #     #  #####   #  #  #  #    #    
#      #    # #      #  #   #     #       #  #  #   # #    #    
#      #    # #    # #   #  #     # #     #  #  #    ##    #    
#       ####   ####  #    # #######  #####  ### #     #    #   

		''')

def check(header, target):
	for i in sites:
		try:
			g=requests.get(i+target)
			if g.status_code==200:
				print(f'found {i+target}')
			else:
				print(f'{i} not found')
		except:
			print(f"Возможно сайт не доступен в вашем регионе {i}")



























def main():
	logo()
	header=initHeaders()
	target=input('target: ')
	check(header, target)
