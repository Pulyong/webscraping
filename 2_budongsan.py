import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
res = requests.get(url)
res.raise_for_status

soup = BeautifulSoup(res.text,"lxml")

rooms = soup.find("table",attrs={"class","tbl"}).find("tbody").find_all("tr")

for ind, room in enumerate(rooms):
    segments = room.find_all("td")
    
    print(f"========== 매물 {ind} ==========")
    print("거래 :",segments[0].get_text() )
    print("면적 :",segments[1].get_text() )
    print("가격 :",segments[2].get_text() )
    print("동 :",segments[3].get_text() )
    print("층 :",segments[4].get_text() )
