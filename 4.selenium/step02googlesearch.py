# 미션 : 구글에서 검색 가능하게 step01 처럼 작업 권장

from selenium import webdriver
import time 

driver = webdriver.Chrome("c:/driver/chromedriver")

driver.get("https://www.google.com/")

tag = driver.find_element_by_name("q")

tag.clear() 

tag.send_keys("AI")
tag.submit()

# 이동된 웹페이지가 실행되는 초단위
time.sleep(20)  # 실행중인 프로그램 중지(sleep)

# 자원 반환 측면에서 driver 도 중지
driver.quit()