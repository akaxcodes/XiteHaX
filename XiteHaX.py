



import os, sys, subprocess,time
import os, sys, json, urllib, re
from time import sleep
os.system("clear")
reload(sys)
sys.setdefaultencoding("utf-8")

# Console colors
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[1m'  # bold
RR = '\033[3m'  # greencolor

def logo():
 print("""

\n\t     \033[31m[_XiteHaX_]
 \n\033[0m\033[1m
\t \033[33m[-] \033[0mPlatform : \033[33mAndroid Termux
\t \033[1m\033[33m[-] \033[0mName     : \033[33mXiteHaX
\t \033[1m\033[33m[-] \033[0mSite     : \033[33www.akash-sharma.in
\t \033[1m\033[33m[-] \033[0mCoded by :\033[1m \033[33m[  \033[32mAkash Sharma\033[33m ]
\t \033[1m\033[33m[-] \033[0mSec.Code : \033[33mAkax Codes\033[0m
  """)


logo()
  

print("""\n\n\n\t\033[33m\033[1m   <===[\033[32m:.Commands.:\033[33m]===>\033[0m
       \n\n1. Initiate XiteHaX    : Website or IP Location Hacker
       \n2. Terminate XiteHaX        : Exit XiteHaX...
\n\n\033[1m\033[32mtype : 1 or 2
       \033[0m""")
def help():
	print("""\n\n
  Commands :
       \n\n1. web     : Website Details Hacker
       \n2. exit        : Exit XiteHaX

\n\n\n type : 1 or 2
       """)





	

XiteHaX = raw_input("\n\n[*] XiteHaX \033[1m\033[33m===>\033[0m ")
if XiteHaX == "help":
            help()

elif XiteHaX == '1':
	print "\n\n\t\033[33m\033[1m <===[\033[32m:.XiteHaX Initiating.:\033[33m]===>\033[0m\n\n\neg. Target\n\n\033[1m\033[33mWebsite\033[0m : www.example.com\n\n\033[1m\033[33mIp\033[0m      : 127.0.0.1"
IP = raw_input("\n\n[*] Website or IP \033[1m\033[33m===>\033[0m")
print "\nHacking\033[1m\033[33m ===> %s" % (IP)
IP2 = IP.split(".")
if IP in ["self", "myself"]:
  urllib.urlretrieve("https://api.ipify.org?format=json", 'data.json')
  file = open('data.json')
  data = json.load(file)
  IP = data["ip"]
urllib.urlretrieve("http://ip-api.com/json/%s" %IP, 'data.json')
file = open('data.json')
data = json.load(file)
if data["status"] != "success": 
  	print "\nSorry!!!  -Please Enter Correct Details...\n\n\033[1m\033[33m  "
  	exit()


	
elif XiteHaX == '2' or XiteHaX == '02' or XiteHaX == 'exit':
	print "\033[1m\033[31m\n\t\t[!] Exit XiteHaX...     \n\n\t\033[1m\033[32m\033[0m"
	sys.exit()
	
else:
	print "\n\n\n\t[!] XiteHaX : \033[32mHacked!!!\033[0m\n\n"

for k in data:
    if data[k] == "": data[k] = "Unknown"
print "\n       *** .: %s :. ***\n\n\n" %data["query"]
print "\nONLINE                         \033[32m\033[1m%s\033[0m    " %data["status"]
print "\nISP                            \033[1m\033[32m%s\033[0m    "%data["isp"]
print "\nORG. NAME                      \033[32m\033[1m%s\033[0m" %data["org"]
print "\nCITY                           \033[32m\033[1m%s\033[0m    " %data["city"]
print "\nCITY TIMEZONE                  \033[32m\033[1m%s\033[0m    " %data["timezone"]
print "\nREGION NAME                    \033[32m\033[1m%s\033[0m" %data["regionName"]
print "\nREGION CODE                    \033[32m\033[1m%s,\033[0m" %data["region"]
print "\nCOUNTRY                        \033[32m\033[1m%s,\033[0m" %data["country"]
print "\nCOUNTRY CODE                   \033[32m\033[1m%s,\033[0m" %data["countryCode"]
print "\nZIP CODE                       \033[32m\033[1m%s\033[0m" %data["zip"]
print "\nLATITUDE                       \033[32m\033[1m%s\033[0m" %data["lat"]
print "\nLONGITUDE                      \033[32m\033[1m%s\033[0m" %data["lon"]
print "\nAS NUMBER/NAME                 \033[32m\033[1m%s\033[0m" %data["as"]
            

print "\n\n\n\n\033[1m\033[32m<=======[ \033[33m\033[1m\033[33m:.Author \033[1m\033[31m:\033[33m Akax Codes.:\033[32m ]=======>\n\n\033[0m"
os.system('rm *.json')
	
sys.exit()
