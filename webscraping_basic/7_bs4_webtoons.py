import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

# lxml Parser를 통해서 res.text를 bs 객체로 만듬
soup = BeautifulSoup(res.text, "lxml")

# attrs에 해당하는 요소를 list로 반환
cartoons = soup.find_all("a", attrs={"class":"title"})

for cartoon in cartoons:
    print(cartoon.get_text())