import requests
import bs4

req = requests.get("https://karnameh.com/car-price")
text = req.text

soup = bs4.BeautifulSoup(text,"html.parser")
s = soup.find_all("p",attrs={"class":"MuiTypography-root MuiTypography-body1 muirtl-iy5bpq"})
s2 = soup.find_all("p",attrs={"class":"MuiTypography-root MuiTypography-body1 muirtl-22intj"})

for i, j in zip(s, s2):
    print(f"{i.text}: {j.text}")