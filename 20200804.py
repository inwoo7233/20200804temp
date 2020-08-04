import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import csv

URL = "https://movie.naver.com/movie/running/current.nhn"
response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

movie_data = []

movie_section = soup.select('dt.tit a')
for a_tag in movie_section: 
    movie_title = a_tag.text

    movie_link = a_tag['href']
    code = movie_link[movie_link.find('code=')+5:]

    movie_tile_code = {
        'title' : movie_title,
        'code' : code
    } 
    movie_data.append(movie_tile_code)

for movie in movie_data:   
    with open('./movie.csv', 'a', newline='') as csvfile:
        fieldnames = ['title','code']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(movie)
    print(f"코드 : {movie['code']}\t[{movie['title']}]")