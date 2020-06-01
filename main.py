import fuckOSINT_byname
import ip
# number
import libs.logo as logo

modes=['1.пробив по имени ', '2.Пробив по ip ']

def main():
	logo.logo()
	for i in modes:
		print(i)
	m=int(input('choose mode '))
	if m==1:
		fuckOSINT_byname.main()
	elif m==2:
		ip.main()

if __name__ == '__main__':
	main()
