import requests
from bs4 import BeautifulSoup

import time #防止短時間內發出大量請求
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
#from selenium.webdriver import Firefox
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.firefox.options import Options
#from selenium.webdriver.support import expected_conditions as expected
#from selenium.webdriver.support.wait import WebDriverWait
chrome_path = "./chromedriver"
url = "https://mojim.com"
#browser = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
browser = webdriver.Chrome(chrome_options = options, executable_path = chrome_path)
browser.get(url)#連到魔鏡歌詞網
#soup = BeautifulSoup(res.text, "html.parser")
#soup = BeautifulSoup(browser.page_source)

singer_class = ["autoA4x", "autoA5x", "autoA6x", "autoA7x"]#歌手列表4個按鈕id
#BoySinger_pointer
#GirlSinger_pointer
#GroupSinger_pointer
#OtherSinger_pointer


#連線到男歌手頁面 將男歌手資料存入BoySingerlist
browser.find_element_by_id("autoA4x").click()
soup = BeautifulSoup(browser.page_source, "lxml")
BoySinger = soup.find('ul', 's_listA').find_all('li')
BoySingerlist = []
for BoySinger_pointer in BoySinger:
	BoySingerlist.append(BoySinger_pointer.text)



#連線到周杰倫
browser.find_element_by_link_text(BoySingerlist[0]).click()
soup = BeautifulSoup(browser.page_source, "lxml")
AR = soup.find_all("span", 'hc3')
for s in AR:
	if s.text == "歌曲列表":
		continue
	tem_song = s.text.split(".")
	for r in tem_song:
		if r == "1":
			continue
		print(r.rstrip("234567890"))


browser.close()

#res = requests.get(url)
#print(res.text)
#soup = BeautifulSoup(res.text, "html.parser")

#type = soup.find(id = 'autoA4x')
#print(type)

#Hello this is Captain America

def test():
	print("Hello")
test()
