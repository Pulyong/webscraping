import requests
from bs4 import BeautifulSoup 
import pandas as pd
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.rc("font",family="Malgun Gothic")
plt.rc('axes', unicode_minus=False)

def show(comment,date,star,good,bad):
    print("내용: "+comment+
        "\n날짜:"+date+
        "\n별점:"+star+
        "\n좋아요:"+good+
        "\n싫어요:"+bad)
    print("-"*50)
def default(url): # url 접속 함수
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")
    return soup

def summary(star_list,good_list,bad_list):
    star_series = pd.Series(star_list)
    good_series = pd.Series(good_list)
    bad_series = pd.Series(bad_list)
    summary = pd.DataFrame({'Star':star_series,'Good':good_series,'Bad':bad_series,'Score':good_series/(good_series+bad_series)})
    return summary

def five_movie_compare(data_list): # 영화제목, 별점 평균
    x = []
    y = []
    for summary,title in data_list:
        x.append(title)
        y.append(summary["Star"].mean())
    plt.figure(figsize=(15,10))
    plt.bar(x,y,color="darkblue",label="대표 네티즌 5명 별점")
    plt.xticks(fontsize=10)
    plt.title('영화 별점 비교')
    plt.ylabel("별점 평균",fontsize=30,loc="bottom",color="cornflowerblue")
    plt.legend(shadow=True,borderpad=1,loc="upper left")
    plt.show() # 대표 네티즌 5명에대한 별점 평균

def all_movie_compare(data_list):
    labels = []
    net = []
    pro = []
    for url in url_movies:
        soup = default(url)
        ratings = soup.find("div",class_="score_area")
        net_rating = ratings.find("div",class_="star_score").find("em").get_text()
        pro_rating = ratings.find_all("div",class_="star_score")[1].find("em").get_text()
        net.append(float(net_rating))
        pro.append(float(pro_rating))
    
    for summary,title in data_list: 
        labels.append(title)
    
    df = pd.DataFrame({
        '영화 제목':labels,
        '네티즌':net,
        '기자ㆍ평론가':pro
    })
    sns.set(font="Malgun Gothic",rc={"axes.unicode_minus":False},style='darkgrid')
    fig,ax1 = plt.subplots(figsize=(10,10))
    tidy = df.melt(id_vars='영화 제목').rename(columns={'variable':'평가자','value':'별점 평균'})
    sns.barplot(x='영화 제목', y='별점 평균', hue='평가자', data=tidy, ax=ax1)
    sns.despine(fig)
    plt.show()
#예매순위 5위까지 접속

url = "https://movie.naver.com/movie/running/current.nhn"
soup = default(url)
page = soup.find("ul",class_="lst_detail_t1")
movies = page.find_all("li",limit=5)
url_movies = []
for movie in movies:
    movie = movie.find("a")["href"]
    url_movie = "https://movie.naver.com/"+movie
    url_movies.append(url_movie)

data_list = [] # plt을 위한 데이터 담기
# 영화 페이지 접속해서 원하는 정보 스크래핑하기
for movie_title,url in enumerate(url_movies):
    soup = default(url)
    star_list = []
    good_list = []
    bad_list = []
    rating_boxs = soup.find("div",class_="score_result").find_all("li")
    title = soup.find("h3",class_="h_movie").find("a").get_text().strip()
    print("#"*50)
    print([title])
    print("링크: "+url)
    for raing_box in rating_boxs:
        comment = raing_box.find("div",class_="score_reple").find("p").get_text().strip()
        date = raing_box.find("div",class_="score_reple").find_all("em")[1].get_text().strip()
        star = raing_box.find("div",class_="star_score").get_text().strip()
        good = raing_box.find("a",class_="_sympathyButton").find("strong").get_text().strip()
        bad = raing_box.find("a",class_="_notSympathyButton").find("strong").get_text().strip()
        star_list.append(int(star))
        good_list.append(int(good))
        bad_list.append(int(bad))
        show(comment,date,star,good,bad)
    movie_title = summary(star_list,good_list,bad_list)
    data_list.append((movie_title,title))

five_movie_compare(data_list)
all_movie_compare(data_list)