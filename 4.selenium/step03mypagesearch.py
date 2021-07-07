

from selenium import webdriver
import time 

driver = webdriver.Chrome("c:/driver/chromedriver.exe")

driver.get("http://127.0.0.1:5500/4.selenium/step03mypage.html")

time.sleep(3)

# input tag
search_box = driver.find_element_by_name('data')

# button tag
btn = driver.execute_script("searchBarModuleClickForSearch()")

# input 에 입력
search_box.send_keys('encore22')

# button 클릭
btn.click()

time.sleep(10)
driver.quit()




for i in range(10):
    time.sleep(1) # 그냥 쉬어감
    proTit = soup.select(“div.title-row > div:nth-child(1) > h5.proTit”)[i].string
    proPrice = soup.select(“div.title-row > div:nth-child(2) > strong.proPrice”)[i].text
    proDays = soup.select(“div.info-row > div:nth-child(1) > p:nth-child(1)“)[i].text
    proDeparture = soup.select(“div.info-row > div:nth-child(1) > p:nth-child(2)“)[i].text
    proScore = soup.select(“div.info-row > div:nth-child(2) > p:nth-child(1)“)[i].text
    print(“제목: “, proTit)
    print(“\n가격: “, proPrice)
    print(“\n여행기간: “, proDays)
    print(“\n출발날짜: “, proDeparture)
    print(“\n점수: “, proScore)
    print(“\n-------------------------------------------------------------------“)