import requests
import bs4

req = requests.get("https://tv.filmnet.ir/")
text = req.text

soup = bs4.BeautifulSoup(text, "html.parser")
s = soup.find_all("h4", attrs={"class": "css-stgv2v eg0dt7k0"})

for i in s:
    print(i.text)