import requests
import bs4

req = requests.get("https://takhfifan.com/tehran/restaurants-cafes")
text = req.text

soup = bs4.BeautifulSoup(text,"html.parser")
s = soup.find_all("p",attrs={"class": "vendor-card-box__title-text"})
s2 = soup.find_all("p",attrs={"class": "rate-badge__rate-value"})

list = {}

for i, j in zip(s, s2):
    print(f"{i.text}:{j.text}")
    list[i.text]= j.text

a = max(list)
print("---------------")
print(f"The highest score belongs to:{a}")