# 동적 페이지 스크래핑
import time, random
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# headless_chrome
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=2560x1440")

driver = webdriver.Chrome(options=options)
driver.maximize_window()

url = "https://play.google.com/store/movies"
headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
        "Accept-Language" : "ko-KR,ko"
}

# 페이지 이동
driver.get(url)

# 자바스크립트 구현

# 지정한 위치로 스크롤 내리기 (1440)
# driver.execute_script("window.scrollTo(0, 1440)") # 해상도에 따른 1페이지 스크롤 다운

# 화면 가장 아래로 스크롤 내리기
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
interval = 2

# 현재 문서 높이 담을 변수
prev_height = driver.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    
    # 스크롤을 가장 아래로 내림
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이 담을 변수
    curr_height = driver.execute_script("return document.body.scrollHeight")

    # 두 높이가 같아지면 탈출
    # prev의 값은 curr보다 항상 작거나 같다
    # 이때 두 값이 같아졌다는 것은 더 이상 내려갈 곳이 없다는 뜻이된다
    if curr_height == prev_height:
        break

    # 기존 높이에 현재 내려온 높이를 넣어줌
    prev_height = curr_height

print("스크롤 완료")
driver.get_screenshot_as_file("google_movie.png")


# 필요없음 => driver.page_source 얘가 대신
# url = "https://play.google.com/store/movies"
# headers = {
#         "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
#         "Accept-Language" : "ko-KR,ko"
#         }

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(driver.page_source, "lxml")

# class를 찾을 때 list를 활용하면 하나 이상의 태그값에 접근할 수 있다.
movies = soup.find_all("div", attrs={"class":"ULeU3b neq64b"})
print(len(movies))

# with open("movie.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify())

time.sleep(random.uniform(1,5))

for movie in movies:
    title = movie.find("div", attrs={"class":"Epkrse"}).get_text()
    print(title)