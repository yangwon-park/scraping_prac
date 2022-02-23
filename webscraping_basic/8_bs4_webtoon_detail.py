import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=783054&weekday=wed"
res = requests.get(url)
res.raise_for_status()

# lxml Parser를 통해서 res.text를 bs 객체로 만듬
soup = BeautifulSoup(res.text, "lxml")

cartoons = soup.find_all("td", attrs={"class":"title"})
# title = cartoons[1].a.get_text()
# link = cartoons[0].a["href"]
# print(title)
# print("https://comic.naver.com" + link)

# 만화 제목 + 링크 가져오기
for c in cartoons:
    title = c.a.get_text()
    link = "https://comic.naver.com" + c.a["href"]
    print(title, link)

# 평점 구하기
star = soup.find_all("div", attrs={"class":"rating_type"})

total = 0

for s in star:
    rate = s.find("strong").get_text()
    print(rate, end = ' ')
    total += float(rate)
print("평균 점수 : ", total / len(star))
