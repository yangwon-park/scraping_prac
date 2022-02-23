# Selenium
- 웹 어플리케이션 테스트를 위한 **Portable Framework**
- 브라우저의 동작을 자동화할 수 있음
- 브라우저별 selenium driver를 별도 설치해야함
    - [Chrome 버전 확인](chrome://version/) (2022-02-23 현재 - 98.0.4758.102)
    - [드라이버 다운로드](https://chromedriver.chromium.org/downloads)
    - 프로젝트 Workspace에 해당 드라이버 실행 파일 옮김 (접근하기 용이하도록)

```python
from selenium import webdriver

# 동일한 경로에 있는 경우 webdriver.Chrome()로 사용 가능
browser = webdriver.Chrome("./chromedriver.exe")

```

## Selenium 기본 기능

**deprecated 관련 에러 발생**

​	- ***[StackOverFlow 참고](https://stackoverflow.com/questions/69875125/find-element-by-commands-are-deprecated-in-selenium)***

```python
from selenium import webdriver
from selenium.webdriver.common.by import By			  # deprecated된 문법 사용하지 않기 위해 불러옴
from selenium.webdriver.common.keys import Keys		  # 키보드로 입력하는 것처럼 사용가능

# 동일한 경로에 드라이버가 있는 경우 webdriver.Chrome()로 사용 가능
driver = webdriver.Chrome()

# find_element_by_* commands are deprecated ~~ => 오래된 문법이므로 권장하지 않음
# elem = browser.find_element_by_class_name("link_login")

# 새로고침
driver.refresh()


# elem = browser.find_element_by_id("query")
elem = browser.find_element(By.ID, "query")
elem.send_keys("입력하고싶은 말")
elem.send_keys(Keys.ENTER)

# 뒤로가기
driver.back()

# 앞으로 가기
driver.forward()

# 탭 하나만 종료
driver.close()

# 탭 전체 종료
driver.quit()
```

