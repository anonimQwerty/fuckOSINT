import fuckOSINT_byname
# number
import libs.logo as logo

modes=['1.пробив по имени ']

def main():
	logo.logo()
	for i in modes:
		print(i)
	m=int(input('choose mode '))
	if m==1:
		fuckOSINT_byname.main()
	elif m==2:
		number.main()

if __name__ == '__main__':
	main()
