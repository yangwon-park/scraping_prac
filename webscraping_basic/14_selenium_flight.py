import time, random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

# 브라우저 실행 후 바로 최대화
# driver.maximize_window()

url = "https://flight.naver.com/"
driver.get(url)

# link_text가 정상 작동 안 해서 모두 XPATH로 처리
# 출발지 선택 
driver.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[1]/button[1]").click()
time.sleep(random.uniform(1,3))
driver.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[9]/div[2]/section/section/button[1]").click()
time.sleep(random.uniform(1,3))
driver.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[9]/div[2]/section/section/div/button[3]").click()
time.sleep(random.uniform(1,3))

# 도착지 선택
# driver.find_element(By.LINK_TEXT, "도착").click()
driver.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]").click()
time.sleep(random.uniform(1,3))
driver.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[9]/div[2]/section/section/button[1]").click()
time.sleep(random.uniform(1,3))
driver.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[9]/div[2]/section/section/div/button[1]").click()
time.sleep(random.uniform(1,3))

# 가는 날 선택 클릭
driver.find_elements(By.CLASS_NAME, "tabContent_option__2y4c6")[0].click()
time.sleep(random.uniform(1,3))
# 이번 달 27일, 28일 선택
driver.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[1]/button/b").click()
time.sleep(random.uniform(1,3))
driver.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[2]/button/b").click()
time.sleep(random.uniform(1,3))

driver.find_element(By.XPATH,"//*[@id='__next']/div/div[1]/div[4]/div/div/button/span").click()

# element가 나올 때까지만 기다려라!
try:
    elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/div[1]/div[5]/div/div[2]/div[2]/div")))
    # 첫 번째 결과 출력
    print(elem.text)
finally:
    driver.quit()

# 첫 번째 결과 출력
# elem = driver.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[5]/div/div[2]/div[2]/div")
# print(elem.text)