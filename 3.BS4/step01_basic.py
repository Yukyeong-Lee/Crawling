html_doc = """<html><head><title>The Dormouse's story</title></head>
# html의 필수 표현법
'''
1. html 문서의 tree 구조로 특정 tag 및 text data 를 찾아가는 형식은 DOM 기반 
2. DOM
    - Document Object Model
    - html 모든 요소(tag, 속성, text..)를 객체로 관리
    - 실시간 가변적인 동적 화면 구성에 필수 핵심 기술
    - 화면을 변경시키는 기술셋
    - 스펙 : w3c에서 제시, 이 dom 기술을 지원하는 개발 언어들은 모든 언어가 다 지원
    - 수업시간엔 js 기반의 dom 처리 학습중
    - id로 특정 tag 검색 : document.getElementById("고유한 id")
    - next_sibling : 현 위치상에서 다음 동생 검색
    - 해킹 필수 기술


        . : class 속성 의미 표기
        # : id 속성의미 표기
        이름 : tag명 의미 표기
'''






html='''

<html>
    <body>
        <h1>스크래핑이란?</h1>
        <p id="one">웹페이지 1</p>
        <p id="two">웹페이지 2</p>
        <span class="redColor">
            <p>웹페이지3</p>
        </span>
        <ul>
            <li><a href="www.daum.net">다음</a></li>
            <li><a href="www.naver.com">네이버</a></li>
        </ul>        
    </body>
</html>
'''

<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
# bs4 - html 문서를 tag, 속성, css 등으로 섬세하게 관리 가능한 API
from bs4 import BeautifulSoup

# 크롤링 대상의 데이터와 구문해석, 문법체크, 변환가능한 parser 설정
soup = BeautifulSoup(html, 'html.parser')
print('--- 1 ---')
print(soup.html.h1)
