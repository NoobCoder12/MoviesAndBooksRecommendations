from dotenv import load_dotenv
import os
import requests
import pandas as pd

load_dotenv()

key = os.getenv('API_KEY')
query = 'batman'

url = "https://api.themoviedb.org/3/search/movie"

params = {
    'api_key': key,
    'query': query
}

# getting movies data
try:
    movies_response = requests.get(url, params=params)
    movies_response.raise_for_status()
    data = movies_response.json()

except Exception as e:
    print(f'Error {e}')


# getting genres data
url_genre = 'https://api.themoviedb.org/3/genre/movie/list'

try:
    response_genres = requests.get(url_genre, params={'api_key': key})
    response_genres.raise_for_status()
    genres = response_genres.json()
except Exception as e:
    print(f'Error {e}')


# mapping genres, dictionary
genres_map = {g['id']: g['name'] for g in genres['genres']}

movies = []

# swapping genres ids for movies with genres
for movie in data['results']:
    title = movie['title']
    genre_ids = movie.get('genre_ids', [])
    genre_names = [genres_map.get(gid, 'Unknown') for gid in genre_ids] 

    for_movies = {"title": title, "genre_ids": genre_ids, 'genre_names': genre_names}
    movies.append(for_movies)

    print(f"Title: {title} -> {', '.join(genre_names) if genre_names else 'No genre'}")



# creating DataFrame for movies and genres

rows = []
for movie in movies:
    row = {'title': movie['title']}
    for gid in genres_map:
        row[genres_map[gid]] = 1 if gid in movie['genre_ids'] else 0
    rows.append(row)

df = pd.DataFrame(rows)

print(df)

