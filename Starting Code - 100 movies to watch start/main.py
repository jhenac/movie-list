import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
greatest_movies = response.text

soup = BeautifulSoup(greatest_movies, "html.parser")

titles = soup.find_all(name="h3", class_="title")
movie_list = [title_tag.getText() for title_tag in titles]
movie_list_reversed = [item for item in reversed(movie_list)]

with open("movie_list.txt", "w", encoding="utf-8") as file:
    for movie in movie_list_reversed:
        file.write(movie + "\n")
