Web Crawling, Web Scraping
============
웹 크롤링과 스크래핑
------------

* 웹 크롤링 - 웹 크롤러(자동화 봇)가 일정 규칙으로 웹페이지를 브라우징 하는 것

* 웹 스크래핑 - 웹 사이트 상에서 원하는 정보를 추출하는 기술

출처 : https://kamang-it.tistory.com/entry/PythonCrawlingScraping%ED%81%AC%EB%A1%A4%EB%A7%81%EA%B3%BC-%EC%8A%A4%ED%81%AC%EB%9E%98%ED%95%91-%EA%B7%B8%EB%A6%AC%EA%B3%A0-%EC%9B%90%EB%A6%AC1

budongsan
------------
### 1. 게임설정

* while문 안에서 input을 받아 원하는 단어를 입력합니다. 보통 행맨게임을 만들 때는 몇개의 단어를 미리 리스트에 입력해 둔 채 코드를 짜는데 저는 재미를 위해 원하는 만큼 단어를 입력할 수 있게 만들었습니다. 입력된 단어는 ask_list라는 리스트 안에 추가됩니다. 

* 단어 추가가 끝나면 "done!"을 입력해 while문을 빠져나옵니다.

* ask_list에 추가된 단어들 중 하나가 random함수를 이용해 무작위로 뽑아 ask라는 변수에 들어가게 됩니다. 그리고 원하는 만큼 life를 지정 할 수 있게 하였습니다.

### 2. 게임 진행

* while문의 조건을 life가 0이 되면 빠져나오게 만들었습니다.

* answer변수에 input으로 단어를 받아 letters변수에 추가됩니다. if문을 통해 기존에 letters변수에 있던 단어를 input받으면 다시 알파벳을 입력하라는 문구가 print되고, letters변수에 없던 알파벳들은 letters변수에 추가되고 정답,오답 문구가 print됩니다.

* for문에서 ask변수의 알파벳 하나하나를 가져와 if문에서 확인하여 ask에 letters에서 입력한 알파벳이 있으면 알파벳을, 없으면 "_"를 end=" "를 이용하여 한줄로 출력할 수 있게 만들었습니다.

* 한번이라도 "_"가 출력되면 succeed를 False로 설정하고 한번도 출력되지 않으면 succeed를 True로 유지하여 succeed가 True면 while문을 break할 수 있도록 만들었습니다.


후기
----

* 파이썬을 배우고 처음으로 조건문과 반복문, random함수등을 이용해 만든 프로그램입니다.

* 다양한 개념을 코드를 직접 만들어 봄으로써 어떤 식으로 개념이 쓰이는지 감을 잡을수 있었습니다.
