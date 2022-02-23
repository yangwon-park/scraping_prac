import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=5&backgroundColor="
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
# print(items[0].find("div", attrs={"class":"name"}).get_text())

for item in items:

    # 광고 제품은 제외
    ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
    if ad_badge:
        print("<광고 제외>")
        continue

    name = item.find("div", attrs={"class":"name"}).get_text()

    # 애플 제품 제외
    if "한성컴퓨터" in name:
        print("<한성컴퓨터> 상품 제외>")
        continue

    price = item.find("strong", attrs={"class":"price-value"})
    rate = item.find("em", attrs={"class":"rating"})

    # 가격이 없는 경우도 있네
    if price:
        price = price.get_text()
    else:
        price = "가격 없음"

    # 평점이 없는 경우도 있음
    if rate:
        rate = rate.get_text()
    else:
        print("<평점이 없는 상품입니다>")
        continue

    rate_cnt = item.find("span", attrs={"class":"rating-total-count"})

    # 평점 수도 마찬가지
    if rate_cnt:
        rate_cnt = rate_cnt.get_text() # 예 : (220) => 이런 식으로 나옴
        rate_cnt = rate_cnt[1:-1]
    else:
        print("<평점이 없는 상품입니다>")
        continue

    # 리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회
    if float(rate) >= 4.5 and int(rate_cnt) >= 100:
        print(name, price, rate, rate_cnt)
