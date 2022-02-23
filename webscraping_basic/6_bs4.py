# beautifulsoap4, lxml 패키지 설치
from pyrsistent import b
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index"
res = requests.get(url)
res.raise_for_status()

# lxml Parser를 통해서 res.text를 bs 객체로 만듬
soup = BeautifulSoup(res.text, "lxml")
print(soup.title)
print(soup.title.get_text())

# 그냥 쓰면 맨 처음 만나는 a 태그를 가지고 옴
print(soup.a.get_text())

# a element의 속성 정보를 dictionary로 반환
print(soup.a.attrs)

# a element의 속성에 접근하여 그 속성값을 반환
print(soup.a["href"])

# 구조를 잘 모를 때는 이렇게 직접 찾자
print(soup.find("a", attrs={"class":"Nbtn_upload"}))

# soup으로 받아온 객체에서 다시 element에 접근 가능
rank1 = soup.find("li", attrs={"class":"rank01"})
print(rank1.a.get_text())

# 개행 정보나 줄바꿈이 있어서 next_sibling 한번으로 안 나오는 경우가 있음
rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling
print(rank3.a.get_text())

# 조건에 해당하는 형제 요소만 찾음 (개행문자에 대한 고려를 할 필요가 없음)
rank2 = rank1.find_next_sibling("li")
print(rank2.a.get_text())

# 마찬가지로 위로도 올라가짐
rank2 = rank3.previous_sibling.previous_sibling
print(rank2.a.get_text())

print(rank1.parent)

webtoon = soup.find("a", text="66666년 만에 환생한 흑마법사-35화 : 유지를 잇는 자")
print(webtoon)