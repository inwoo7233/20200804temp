import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import csv

URL = "https://movie.naver.com/movie/running/current.nhn"
response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

movie_data = []

movies = soup.select('dt.tit a')
for a_tag in movies: 
    title = a_tag.text

    link_split = a_tag['href'].split('=')
    code = link_split[1]
    movie_tile_code = {
        'title' : title,
        'code' : code
    } 
    movie_data.append(movie_tile_code)

for movie in movie_data:   
    with open('./movie.csv', 'a', newline='') as csvfile:
        fieldnames = ['title','code']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(movie)
    print(f"코드 : {movie['code']}\t[{movie['title']}]")