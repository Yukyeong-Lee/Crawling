from flask import Flask, request, render_template, jsonify
import time
from bs4 import BeautifulSoup
from selenium import webdriver

app = Flask(__name__)


@app.route('/', methods=['get'])
def get():
    print('get')
    return render_template('index.html')  


@app.route('/getdata', methods=['post'])
def getdata():
    driver = webdriver.Chrome("C:/driver/chromedriver")
    driver.get('https://www.nike.com/kr/launch/?type=upcoming')
    time.sleep(3) 
    # print(driver.page_source)
    # driver.implicitly_wait(10) # seconds
    soup = BeautifulSoup(driver.page_source, 'lxml')

    boxitems = soup.find(class_='item-list-wrap').find_all('li')
    print('--'*30)
    # print(boxitems[0])
    items=[]
    for boxitem in boxitems[:4]:
        name = boxitem.find(class_='copy-container').h6.text    # tag끼리는
        img = boxitem.find(class_='card-link').img.attrs['src']
        # print(img)
        items.append({'name' : name, 'img' : img})
    # print(items)
    print(items)
    return jsonify(items)




if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port="5000")