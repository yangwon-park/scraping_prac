import requests
from bs4 import BeautifulSoup

for year in range(2015, 2020):
    url = 'https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR'.format(year)
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}

    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class":"thumb_img"})


    # 인덱스 번호와 각 요소를 함께 튜플 형태로 반환
    for idx, image in enumerate(images):
        # print(i["src"])
        image_url = image["src"]

        if image_url.startswith("//"):
            image_url = "https:" + image_url

        # print(image_url)

        # 이미지 경로에 다시 접근
        image_res = requests.get(image_url)
        image_res.raise_for_status()

        # 단순히 idx로만 구분했을 경우 이름이 덮어써져서 5개만 파일이 생성됨
        with open("movie_{}_{}.jpg".format(year, idx+1), "wb") as f:
            f.write(image_res.content)

        if idx >= 4:
            break