# 정적 페이지 스크래핑
import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies"
headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
        "Accept-Language" : "ko-KR,ko"
        }
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"ULeU3b neq64b"})
print(len(movies))

# with open("movie.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify())

for movie in movies:
    title = movie.find("div", attrs={"class":"Epkrse"}).get_text()
    print(title)