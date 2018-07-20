import requests
from bs4 import BeautifulSoup

def main():
	resp = requests.get("http://blog.castman.net/web-crawler-tutorial/ch2/blog/blog.html")
	soup = BeautifulSoup(resp.text,"html.parser")
	"""
	#取得第一篇h4
	print(soup.find("h4"))
	print(soup.h4)
	
	#取得第一篇h4 不包含tag
	print(soup.h4.a.text)
	
	#取得所有h4
	main_titles = soup.find_all("h4")
	for title in main_titles:
		print(title.a.text)
	
	#取得所有class為card-title的h4
	#soup.find_all('h4', {'class': 'card-title'})
	#soup.find_all('h4', class_='card-title')
	main_titles = soup.find_all("h4","card-title")
	for title in main_titles:
		print(title.a.text)
	
	#取得第一篇id為mac-p的元件
	print(soup.find(id = "mac-p"))
	"""
	#取得各篇blog所有文字
	divs = soup.find_all('div','content')
	for div in divs:
		#print(div.text)
		print(div.h6.text.strip(), div.h4.a.text.strip(), div.p.text.strip())
		#print([s for s in div.stripped_strings])

if __name__=='__main__':
	main()
