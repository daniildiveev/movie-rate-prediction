import json
from parsers import *

url = "https://www.kinopoisk.ru/lists/movies/country--1/?ss_subscription=ANY"

movie_links = parse_links(url)
descriptions, rates, genres = parse_data(movie_links, 2)

data = {
    'descriptions' : descriptions,
    'rates' : rates, 
    'genres' : genres
}

with open("descriptions_rates_and_genres.json", "w") as f:
    json.dump(data, f)