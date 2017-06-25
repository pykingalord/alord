import socket
import os
os.system("cls")
os.system('color a')
print('\n welcom to sock Tool \n')
bannar = """

                      _    
       ___  ___   ___| | __
      / __|/ _ \ / __| |/ /
      \__ \ (_) | (__|   < 
      |___/\___/ \___|_|\_\ 
                     
     1 get name port

     2 get number port

     3 get ip address inset

     4 get name computer

     5 get name computer and domin and ip address

     6 get DNS website

     7 ping in website

     8 exit


"""
print (bannar)
get = input('sock >')
if get == 1:
	input_one = input('\nEnter your number port :')
	print ('name port is >>',socket.getservbyport(input_one))
if get == 2:
	input_tow = input('Enter your name port <example ("ftp")> :')
	a = str(input_tow)
	print ('number port is >>',socket.getservbyname(a))
if get == 3:
	input_three = input('Enter your name computer <example ("hacker")> :')
	print ('ip address >>',socket.gethostbyname(input_three))
if get == 4:
	print ('name computer >>',socket.gethostname())
if get ==5:
	input_four = input('Enter your ip address <example ("127.0.0.1")> :')
	print ('inforamtin >',list(socket.gethostbyaddr(input_four)))
if get == 6:
	input_5 = input('Plase enter your website domin <example(google.com)> :')
	print ('DNS websire >>',socket.getaddrinfo(input_5,'www'))
if get == 7:
	name = input("Plase enter your website :")
	name = socket.gethostbyname(name)
	print(os.system('ping -n 1000000',name))
if get == 8:
	exit()
if get > 8:
	print ('\nError not found your number')
