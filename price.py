import requests
from bs4 import BeautifulSoup as bs4

res = requests.get("http://blog.castman.net/web-crawler-tutorial/ch2/table/table.html")
soup = bs4(res.text, "html.parser")

prices = []
links = soup.find_all('a')
for link in links:
    price = link.parent.previous_sibling.text
    prices.append(int(price))
print(sum(prices) / len(prices))

rows = soup.find("table", "table").tbody.find_all("tr")
for row in rows:
    print([s for s in row.stripped_strings])


