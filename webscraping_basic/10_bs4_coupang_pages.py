import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}

# 1 ~ 5 페이지까지 확인
for i in range(1, 6):
    print("현재 페이지 : ", i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=5&backgroundColor=".format(i)

    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

    for item in items:

        # 광고 제품은 제외
        ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
        if ad_badge:
            #print("<광고 제외>")
            continue

        name = item.find("div", attrs={"class":"name"}).get_text()

        # 애플 제품 제외
        if "한성컴퓨터" in name:
            #print("<한성컴퓨터> 상품 제외>")
            continue

        price = item.find("strong", attrs={"class":"price-value"})
        rate = item.find("em", attrs={"class":"rating"})

        # 가격이 없는 경우도 있네
        if price:
            price = price.get_text()
        else:
            #print("<가격이 없는 상품입니다>")
            continue

        # 평점이 없는 경우도 있음
        if rate:
            rate = rate.get_text()
        else:
            #print("<평점이 없는 상품입니다>")
            continue

        rate_cnt = item.find("span", attrs={"class":"rating-total-count"})

        # 평점 수도 마찬가지
        if rate_cnt:
            rate_cnt = rate_cnt.get_text() # 예 : (220) => 이런 식으로 나옴
            rate_cnt = rate_cnt[1:-1]
        else:
            #print("<평점이 없는 상품입니다>")
            continue

        link = item.find("a", attrs={"class":"search-product-link"})["href"]

        # 리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회
        if float(rate) >= 4.5 and int(rate_cnt) >= 100:
            #print(name, price, rate, rate_cnt)
            print(f"제품명 : {name}")
            print(f"가격 : {price}")
            print(f"평점  : {rate} ({rate_cnt} 개")
            print("바로가기 : {}".format("https://www.coupang.com" + link))
            print("-"*100) # 경계선
            