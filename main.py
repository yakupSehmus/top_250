import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"
response = requests.get(url)

hmtl_icerigi = response.content

soup = BeautifulSoup(hmtl_icerigi, "html.parser")

for i in soup.find_all("td",{"class":"titleColumn"}):
    print(i.text)
