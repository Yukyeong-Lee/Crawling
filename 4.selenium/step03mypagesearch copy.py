

from selenium import webdriver
import time 

driver = webdriver.Chrome("c:/driver/chromedriver.exe")
driver.get("http://tour.interpark.com/")
# 검색창 선택
search_box = driver.find_element_by_id("SearchGNBText")
# time.sleep(1)
# 입력
search_box.send_keys("파리")
# time.sleep(1)
# 검색 script 실행
driver.execute_script("searchBarModule.ClickForSearch()")
# html 을 받아옴
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# 상위 10개 제목을 뽑음
for i in range(10):
driver.execute_script("searchModule.SetCategoryList({}, '')".format(target_page))
   
print("\n{}번째 페이지의 크롤링을 시작합니다.\n".format(target_page))
    
boxItems = driver.find_elements_by_css_selector('.panelZone > .oTravelBox > .boxList > li')
    
for li in boxItems:
        # print('상품명 :', li.find_element_by_css_selector('h5.proTit').text)
    title = li.find_element_by_css_selector('h5.proTit').text
        # print('가격 :', li.find_element_by_css_selector('.proPrice').text.split('원')[0])
    price = li.find_element_by_css_selector('.proPrice').text.replace(',','').replace('원~','')