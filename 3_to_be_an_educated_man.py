import requests
from bs4 import BeautifulSoup
import re

def default(url): # url 접속 함수
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36" }
    res = requests.get(url,headers=headers)
    res.raise_for_status
    soup = BeautifulSoup(res.text,"lxml")
    return soup

def weather_info(): #날씨정보 함수
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%9D%B8%EC%B2%9C+%EC%84%9C%EA%B5%AC+%EB%82%A0%EC%94%A8"
    soup = default(url)
    weather1 = soup.find("div",attrs={"class","today_area _mainTabContent"})
    compare = weather1.find("p",attrs={"class","cast_txt"}).get_text()
    pre_temp = weather1.find("span",attrs={"class","todaytemp"}).get_text()+"℃"
    min_temp = weather1.find("span",attrs={"class","min"}).get_text()
    max_temp = weather1.find("span",attrs={"class","max"}).get_text()
    rain_rate_mon = soup.find("ul",attrs={"class","list_area _pageList"}).find("span",attrs={"class":"point_time morning"}).find("span",attrs={"class":"num"}).get_text()+"%"
    rain_rate_aft = soup.find("ul",attrs={"class","list_area _pageList"}).find("span",attrs={"class":"point_time afternoon"}).find("span",attrs={"class":"num"}).get_text()+"%"
    dust = weather1.find_all("dd",attrs={"class","lv1"})[0].get_text()
    cho_dust = weather1.find_all("dd",attrs={"class","lv1"})[1].get_text()
    print("[오늘의 날씨]")
    print(compare)
    print(f"현재 {pre_temp}  (최저 {min_temp} / 최고 {max_temp})")
    print(f"오전 강수확률 {rain_rate_mon} / 오후 강수확률 {rain_rate_aft}")
    print()
    print(f"미세먼지 {dust}")
    print(f"초미세먼지 {cho_dust}")
    print()

def headline_news(): # 뉴스정보
    url = "https://news.naver.com/"
    soup = default(url)
    news = soup.find("ul",attrs={"class":"hdline_article_list"}).find_all("li")
    for new in news:
        headline = new.find("div",attrs={"class":"hdline_article_tit"})
        link = headline.find("a")["href"]
        print("[헤드라인 뉴스]")
        print(headline.get_text().strip())
        print("https://news.naver.com/"+link)
    print()

def IT_news(): # IT뉴스
    url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = default(url)
    news = soup.find("ul",attrs={"class":"type06_headline"}).find_all("li",limit=3)
    for new in news:
        headline = new.find_all("dt")[1]
        link = headline.find("a")["href"]
        print("[IT 뉴스]")
        print(headline.get_text().strip())
        print(link)
    print()

def English():
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english#;"
    soup = default(url)
    korean = soup.find("div",attrs={"class":"conv_txt"}).find_all("div",attrs={"id":re.compile("^conv_kor")})
    english = soup.find_all("div",attrs={"class":"conv_txt"})[1].find_all("div",attrs={"id":re.compile("^conv_kor")})
    print("(영어지문)")
    for eng in english:
        eng = eng.get_text().strip()
        print(eng)
    print("(한글지문)")
    for korea in korean:
        korea = korea.get_text().strip()
        print(korea)
    

if __name__ == "__main__":
    weather_info()
    headline_news()
    IT_news()
    English()
