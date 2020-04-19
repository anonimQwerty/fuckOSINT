import os, fuckOSINT_byname

modes=['1.пробив по имени ']

















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


def main():
	logo()
	for i in modes:
		print(i)
	m=int(input('choose mode '))
	if m==1:
		fuckOSINT_byname.main()




if __name__ == '__main__':
	main()