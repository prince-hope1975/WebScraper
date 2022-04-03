import requests
from bs4 import BeautifulSoup

URL = "https://algoexplorer.io/address/EJNUC2EMTEZTPWJH6ZYOGQKHJBKHAZGSDEJZO4QHRO26RQWHW2ZTYHX4A4"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup

file = open("index.html", "w")
file.write(soup.prettify())
file.close()

print(results.prettify())
# print(page.text)
