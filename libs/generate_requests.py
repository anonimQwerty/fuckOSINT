import users_agents as users_agents
import random, requests, json








def generate_request():
	user=random.choice(users_agents.headers_useragents)
	requests_list={
'name':['instagram', 'vk'],
'link':['https://www.instagram.com/'],
'headers':[
{
	'Accept':'*/*',
	'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
'Cache-Control':'no-cache',
'Connection':'keep-alive',
'Content-Length':'293',
'Content-Type':'application/x-www-form-urlencoded',
'Cookie':'ig_cb=1; ig_did=FEA830C5-E633-42C9-AFE0-03942A43257E; csrftoken=5bTq2aCiosADYwDx5RvyuV2LqgYUCoXZ; rur=VLL; mid=XpxVVQAEAAE_-uDoKOO4k2X3uu4T',
'DNT':'1',
'Host':'www.instagram.com',
'Pragma':'no-cache',
'Referer':'https://www.instagram.com/',
'User-Agent':user,
'X-CSRFToken':'5bTq2aCiosADYwDx5RvyuV2LqgYUCoXZ',
'X-IG-App-ID':'936619743392459',
'X-IG-WWW-Claim':'0',
'X-Instagram-AJAX':'cc6f59f85f33',
'X-Requested-With':'XMLHttpRequest',



}




],
'data':[
{
'enc_password':'#PWD_INSTAGRAM_BROWSER:6:1587303903:AZtQAH4dKKi93th04DCNSVaQhS3rbbNrXfisGYgLUOg1zHg/T7s6guC3UHVPiZRVtfjwrmmsbpGYJurt/Qa/gFlh8gBBQhx0M/IEQQy+bp9k9jGtfs7NvD8eghz6Itmf2uMGCrbLwMLZ8IDI',
'optIntoOneTap':'false',
'password':'rttyhyuy',
'queryParams':'{}',
'username':'+380987262484'}

],
'answer':[]


	}
	return requests_list

	
a=generate_request()
s=requests.Session()
site=a['link'][0]
headers=a['headers'][0]
data=a['data'][0]
r=s.post(site, headers=headers, data=data)

#print(r.content)
#print(r.text)
#print(r.status_code)
print(r.content)