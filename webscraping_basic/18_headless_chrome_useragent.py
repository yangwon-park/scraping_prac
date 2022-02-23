from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=2560x1440")

# 밑의 코드로 user-agent를 직접 설정해주지 않으면
# Chrome이 아니라 HeadlessChrome으로 나와서 서버에서 막을 수도 있다
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36")

driver = webdriver.Chrome(options=options)
driver.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
driver.get(url)

id = driver.find_element_by_id("detected_value")
print(id.text)
driver.quit()