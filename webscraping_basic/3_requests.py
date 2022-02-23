import requests
from sqlalchemy import false


#   InsecureRequestWarning: Unverified HTTPS request is being made to host
#   이런 에러가 터미널에 발생하는데 경고의 의미이므로 일단은 무시하자
url = "http://google.com"
res = requests.get(url)

# 올바르게 실행되면 정상 실행
# 아닌 경우 에러 => 프로그램이 종료됨
res.raise_for_status()
print("웹 스크래핑을 진행합니다.")

# print("응답 코드  : ", res.status_code) # 200 뜨나 확인


# if res.status_code == requests.codes.ok:
#     print("정상")
# else:
#     print(res.status_code)

print(len(res.text))
print(res.text)

# res.url의 정보를 가지고옴 (스타일은 망가짐)
with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)