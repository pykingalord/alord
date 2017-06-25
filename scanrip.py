import socket , sys
from datetime import datetime
import os
from optparse import OptionParser
os.system("title scanrip Hacking programming python")
os.system("color a")
os.system('cls')
print("\t\n")
print("  sSSs    sSSsS  .S_SSSs     .S_sSSs     .S_sSSs     .S   .S_sSSs      ")
print(" d//SP   d//SP  .SS~SSSSS    .SS~YS//b   .SS~YS//b   .SS  .SS~YS//b    ")
print(" d%t'    d%4'    S%7   SSSS  S%6   `S%4  S%3   `S%6  S%1  S%+   `S%0   ")
print(" S%|     S%6     S%9    S%7  S%8    S%-  S%`    S%1  S%5  S%6    S%9   ")
print(" S&S     S&S     S%8 SSSS%6  S%0    S&S  S%6    d*S  S&S  S%5    d*S   ")
print(" Y&Ss    S&S     S&S  SSS%5  S&S    S&S  S&S   .S*S  S&S  S&S   .S*S   ")
print("`S&&S    S&S     S&S    S&S  S&S    S&S  S&S_sdSSSA  S&S  S&S_sdSSS    ")
print("  `S*S   S&S     S&S    S&S  S&S    S&S  S&S~YSY%9W  S&S  S&S~YSSY     ")  
print("   l*S   S*b     S*S    S&S  S*S    S*S  S*S   `S%3  S*S  S*S          ")
print("   S*P   S*S.    S*S    S*S  S*S    S*S  S*S    S%2  S*S  S*S          ")
print(" sSS*S   SSSb    S*S    S*S  S*S    S*S  S*S    S&S  S*S  S*S          ")
print(" YSS'    YSSPS   SSS    S*S  S*S    SSS  S*S    SSS  S*S  S*S          ")
print("                        SP   SP          SP          SP   SP           ")
print("                        Y    Y           Y           Y    Y            ")
print("\t\n")
print("A-Domain name scan\t\t\tB-IP address scan\nC-Bring url and IP address\t\nE-exit")
d = raw_input("Press Enter the Character :")
if (d == 'A' or d == 'a'):
	rmserver = raw_input("\t Enter the Domin name to scan :\t")
	rmip = socket.gethostbyname(rmserver)
elif (d == 'B' or d == 'b'):
	rmip = raw_input("\t Enter the remote host IP to scan :")
elif (d == 'C' or d == 'c'):
	sock1 = raw_input("\t Enter the IP address :")
	sock2 = socket.gethostbyaddr(sock1)
	print(sock2)
	sys.exit()
elif (d == 'E' or 'e'):
	sys.exit()
elif (d == 'A' or d == 'a' or d == 'B' or d == 'b'):
	print ("Wrong input")
r1 = int(raw_input(" [1] Enter the start port number :"))
r2 = int(raw_input(" [2] Enter the last port number :"))
print ("-"*50)
print ("\n [+] Port scanner working on :",rmip)
print ("-"*50)
t1 = datetime.now()
try:
	for port in range(r1,r2):
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = sock.connect_ex((rmip,port))
		if result == 0:
			print (" [*] port Open -> \t",port,"name is ->",socket.getservbyport(port))
		sock.close()
except KeyboardInterrupt:
	print ("You stop this")
	print("port closed",rmip,"--",socket.getservbyport(port))
	sys.exit()
except socket.gaierror:
	print ("Hostname could not be resolver")
	sys.exit()
except socket.error:
	print ("could not connect to server ")
	sys.exit()
t2 = datetime.now()
total = t2 - t1
print ("Scanning Complete in :",total)


