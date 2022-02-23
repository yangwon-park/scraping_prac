import time, random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("./chromedriver.exe")
time.sleep(random.uniform(1, 3)) # delay

# 1. 네이버 이동
driver.get("http://naver.com")

# 2. 로그인 버튼 찾고 누르기 (로그인 페이지로 화면 전환)
elem = driver.find_element(By.CLASS_NAME, "link_login")
elem.click()

# 3, 4로 하면 naver Captcha에 걸려서 자동입력 방지 문자 입력 페이지로 넘어감
# 3. 아이디, 비밀번호 ID 찾은 후 로그인하기
time.sleep(random.uniform(1, 3)) # delay
driver.find_element(By.ID, "id").send_keys("test_id")
driver.find_element(By.ID, "pw").send_keys("test_pw")

# 4. 로그인 버튼 클릭
time.sleep(random.uniform(1, 3)) # delay
driver.find_element(By.ID, "pw").submit()

# # 아래와 같이 javascript를 활용하여 우회
# 현재 얘도 막힘
# input_js = '\
#             document.getElementById("id").value = "{id}"; \
#             document.getElementById("pw").value = "{pw}"; \
#     '.format(id="test_id", pw="test_pw")
# time.sleep(random.uniform(1,3))
# driver.execute_script(input_js)
# time.sleep(random.uniform(1,3))
# driver.find_element(By.ID, "log.login").click()

# 5. 로그인 실패 시, 새로운 아이디를 입력하기 위한 clear
driver.find_element(By.ID, "id").clear()
driver.find_element(By.ID, "id").send_keys("my_id")

# 6. html 정보 출력
print(driver.page_source)

# 7. 브라우저 종료
driver.quit()


