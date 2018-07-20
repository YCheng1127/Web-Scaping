import requests
from bs4 import BeautifulSoup as bs4

import time
import singerandhref

#fix SSLError failed
#import socket
#import socks
#socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 1080)
#socket.socket = socks.socksocket

#fix SSLError success
try:
	import urllib3.contrib.pyopenssl
	urllib3.contrib.pyopenssl.inject_into_urllib3()
except ImportError:
	pass

Mojim = "https://mojim.com"
headers = {"User-Agent": "User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}

classlist = []#record the search_page
classlist.append("http://mojim.com/twza1.htm")#first for boysinger
classlist.append("http://mojim.com/twzb1.htm")#second for girlsinger
#print(classlist)

res = requests.get(classlist[0], headers = headers, timeout = 20)
#print(res.text)

soup = bs4(res.text,"html.parser")
#A = soup.find('ul',"s_list").find_all('a')
#for r in A:
#	print(r.get("href"))
#I tried to get href by soup, but it seems that the href is too easy to guest

#build B_alphabet_list
def get_Boy_singer_alphabet_href():
	B_alphabet_list=[]
	for r in range(39):
		if r == 0:
			continue
		elif r == 1:
			B_alphabet_list.append("https://mojim.com/twza1.htm")
		elif r > 1 and r < 10:
			B_alphabet_list.append("https://mojim.com/" + "twzlha1_0" + str(r) + ".htm")
		else:
			B_alphabet_list.append("https://mojim.com/" + "twzlha1_" + str(r) + ".htm")
	return B_alphabet_list
#print(get_Boy_singer_alphabet_href())	測試function	 

#build a Singerlist about name and href	輸入注音連結 可以得到歌手清單，回傳歌手(.name)與連結(.href)結構
def get_singer_list(alphabet_url):
	Singer_pointer = []
	res = requests.get(alphabet_url, headers = headers, timeout =10)#B_alphabet_list[0]
	soup = bs4(res.text, "html.parser")
	B = soup.find('ul', 's_listA').find_all('a')
	for r in B:
		SingerX = singerandhref.singerandhref(r.text, Mojim + r.get("href"))
		Singer_pointer.append(SingerX)		
	return Singer_pointer
#K = get_singer_list(B_alphabet_list[1]) 測試function
#for k in K:
#	print(k.name)

#go to the song page   輸入歌手名連結，可回傳歌單(.name)與歌詞(.href)連結(結構) 
def get_Song_pointer(singer):
	Song_pointer = []
	res = requests.get(singer.href, headers = headers, timeout = 10)	#"https://mojim.com/twh100951.htm"
	soup = bs4(res.text, "html.parser")
	C = soup.find_all("span",["hc3", "hc4"])
	A_list = []
	for q in C:
		fetch_a = q.find_all('a')
		for n in fetch_a:
			A_list.append(n)
	for q in A_list:
		SongX = singerandhref.songandhref(q.text, Mojim + q.get("href"))
		Song_pointer.append(SongX)
	return Song_pointer

#M = get_Song_pointer("https://mojim.com/twh100951.htm") 測試function
#for g in M:
#	print(g.name)

def tide_lyric(tok):
	tok_process = str(tok).replace('<br/>', '\n')
	tok_process = tok_process.replace('<a href="http://mojim.com">※ Mojim.com　魔鏡歌詞網 </a>', '')
	tok_process = tok_process.replace('更多更詳盡歌詞 在', '')
	tok_process = tok_process.replace('<dd id="fsZx3" class="fsZx3">', '')
	#刪除tag
	while True:
		index_begin = tok_process.find("<")
		index_end = tok_process.find(">", index_begin + 1)
		if index_begin == -1:
			break
		tok_process = tok_process.replace(tok_process[index_begin:index_end+1], '')
	#刪除 作詞作曲
	for check_label in range(7):
		index_begin = tok_process.find("")
		index_end = tok_process.find("\n", index_begin + 1)
		tem_tok = tok_process[index_begin:index_end+1]
		if tem_tok.find("歌名") != -1 or tem_tok.find("作詞") != -1 or tem_tok.find("作曲") != -1 or tem_tok.find("編曲") != -1 or tem_tok.find("演唱") != -1:
			tok_process = tok_process.replace(tem_tok, '')
			
	#刪除 時間軸
	while True:
		index_begin = tok_process.find("[")
		index_end = tok_process.find("\n", index_begin + 1)
		tem_tok = tok_process[index_begin:index_end+1]	
		if index_begin == -1:
			break 
		tok_process = tok_process.replace(tem_tok, '')
	#刪除 感謝 最後一行
	for check_label in range(1):
		index_end = tok_process.rfind("\n")
		tem_tok = tok_process[0:index_end]
		index_begin = tem_tok.rfind("\n")
		tok_process = tok_process[0:index_begin]
		
		#index_end = tok_process.find("\n", index_begin+1)
		#print(index_begin)
		#tem_tok = tok_process[index_begin:index_end+1]
		#print(tem_tok)	

	return tok_process

#fetch lyrics
def fetch_lyrics(lyric):
	try:
		res = requests.get(lyric.href, headers = headers, timeout = 10)
		
	except requests.exceptions.ConnectionError:
		print("ConnectionError -- please wait 3 seconds")
		time.sleep(3)
	
	soup = bs4(res.text, "html.parser")
	D = soup.find(id = "fsZx3")
	
	try:
		D_process = tide_lyric(D)
	except AttributeError:
		print("cannot get text of id(fsZx3)")
		return "cannot get text of id(fsZx3)"
	else:	
		print("歌名: " + lyric.name)
		print(D_process)
		return "歌名: " + lyric.name + "\n" + D_process
#fetch_lyrics("https://mojim.com/twy102201x9x16.htm") 測試function
Singer_record = []

f = open("lyric.txt", "w")
num = 1
alphabet_href = get_Boy_singer_alphabet_href()
for rat in alphabet_href:
	singerlist = get_singer_list(rat)
	for cow in singerlist:
		syn = 0
		for detect_repeat in Singer_record:
			if detect_repeat == cow.name:
				syn = syn + 1
		if syn == 0:	
			songlist = get_Song_pointer(cow)
			Singer_record.append(cow.name)

		for tiger in songlist:
			outcome = fetch_lyrics(tiger)
			if len(outcome) > 50:
				print("\n" + str(num) +  ".\n" + "歌手: " + cow.name)
				f.write("\n" + str(num) + ".\n" + "歌手: " + cow.name + "\n")
				f.write(outcome)
				num = num + 1

#SS = singerandhref.songandhref("你們要快樂", "https://mojim.com/twy102201x9x16.htm")
#fetch_lyrics(SS)

