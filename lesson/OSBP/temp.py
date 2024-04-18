from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 웹 드라이버를 초기화합니다.
driver = webdriver.Chrome() 
# 로그인 페이지로 이동합니다.
driver.get('https://sw7up.cbnu.ac.kr/account/login')

# body 태그를 선택합니다.
body = driver.find_element_by_tag_name('body')

# 탭 키를 누르고, 아이디를 입력합니다.
body.send_keys(Keys.TAB + '2021076002')  # 'your_username'은 실제 아이디로 변경해야 합니다.

# 탭 키를 누르고, 비밀번호를 입력합니다.
body.send_keys(Keys.TAB + 'QWerTY141!')  # 'your_password'은 실제 비밀번호로 변경해야 합니다.

# 탭 키를 누르고, 엔터 키를 누릅니다.
body.send_keys(Keys.TAB + Keys.ENTER)

# 브라우저가 종료되지 않도록 대기합니다.
time.sleep(10)  # 예시로 10초 동안 대기하도록 설정했습니다.

# 드라이버를 종료합니다.
driver.quit()