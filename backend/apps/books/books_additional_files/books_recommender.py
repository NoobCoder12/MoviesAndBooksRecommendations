import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from .genresMatrix import subject_to_keywords
import os
import pickle
import time
import json


CACHE_FILE = 'cache_books.pkl'  # nazwa pliku
EXPIRATION_SECONDS = 1 # ilość czasu, jaką jest pozycja w cache


#  załadowanie cache, jeśli jest
if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, 'rb') as f:
        cache = pickle.load(f)

else:
    cache = {}


def fetch_best_book_category(title):
    now = time.time()  # aktualny timestamp (sekundy od 1970)
    # zmiana tytułu na małe litery bez spacji na początku i końcu
    title = title.lower().strip()

    # sprawdzenie, czy pozycja jest już w cache, słownik w słowniku
    if 'titles' in cache and title in cache['titles']:
        entry = cache['titles'][title]  # przypisanie do zmiennej

        # sprawdzenie czy mieści się w zakresie czasowym
        if now - entry['timestamp'] < EXPIRATION_SECONDS:
            return entry['result']  # zwrócenie pozycji z cache

    # przygotowanie tytułu i wyszukanie w API
    title_query = title.replace(' ', '_')
    url = f"https://openlibrary.org/subjects/{title_query}.json"

    try:
        response = requests.get(url)
        response.raise_for_status()  # w przypadku błędu będzie HTTPError
        data = response.json()
    except Exception as e:
        print(f'Error fetching data: {e}')
        return []

    subjects = [' '.join(work.get('subject', []))
                for work in data.get('works', [])]  # pobranie gatunków przypisanych do książki

    # stworzenie formatu pozycji w cache
    if 'titles' not in cache:
        cache['titles'] = {}
    cache['titles'][title] = {'timestamp': now, 'result': subjects}

    with open(CACHE_FILE, 'wb') as f:
        pickle.dump(cache, f)  # zapisanie pozycji do cache

    title_stop = title.lower().split()  # przygotowanie tytułu jako stop word
    custom_stop_words = ['english', 'en', 'literature', 'novel', 'criticism',
                         'motion', 'picture', 'pictures', 'film', 'video',
                         'adaptation', 'adaptations', 'films', 'movie', 'movies',
                         'cinema', 'dvd', 'blu-ray', 'edition', 'collection',
                         'game', 'games', 'videogames', 'playstation', 'xbox',
                         'general', 'fiction', 'works', 'pictorial', 'illustrations',
                         'study', 'criticism', 'analysis', 'companion', 'guide',
                         'book', 'books', 'reading', 'library'] + title_stop  # stworzenie listy stop words

    stop_words = list(ENGLISH_STOP_WORDS) + (custom_stop_words)

    genres_values = [' '.join(words) for words in subject_to_keywords.values()] # połączenie wartości per klucz z matrycy w listę
    genres_labels = list(subject_to_keywords.keys()) # połączenie gatunków w listę

    # tworzenie obiektu dla wektora, nie ingoruje zadnego słowa
    vectorizer = TfidfVectorizer(stop_words=stop_words, max_df=1.0, min_df=1)
    # trenowanie i przekształcanie gatunków w matrycę
    genres_matrix = vectorizer.fit_transform(genres_values)

    subjects_joined = [' '.join(subjects)] # lista połączonych gartunków
    book_matrix = vectorizer.transform(subjects_joined) # matryca z listy połączonych gatunków

    similarity = cosine_similarity(book_matrix, genres_matrix) # liczymy podobienstwo z główną matrycą
    scores = similarity[0] #tworzymy listę 1d z 2d
    results = list(zip(genres_labels, scores)) # dopasowujemy w liście gatunek -> wynik podobienstwa
    results_sorted = sorted(results, key=lambda x: x[1], reverse=True) # sortowanie po drugim elemencie krotki, malejąco
    top_categories = [element[0] for element in results_sorted] # wybór kategorii z kazdej krotki
    top_category = top_categories[0] 

    return top_category


def fetch_books_by_category(category):
    now = time.time()  # aktualny timestamp (sekundy od 1970)
    # zmiana tytułu na małe litery
    category = category.lower()

    # sprawdzenie, czy jest już taki słownik i podsłowniki z żądanym gatunkiem
    if 'genres' in cache and category in cache['genres']:
        entry = cache['genres'][category]  # przypisanie zmiennej
        if now - entry['timestamp'] < EXPIRATION_SECONDS:

            return entry['result']  # zwrócenie pozycji, jeśli jest

    url = f"https://openlibrary.org/subjects/{category}.json"

    try:
        response = requests.get(url)
        response.raise_for_status()  # w przypadku błędu będzie HTTPError
        data = response.json()
    except Exception as e:
        print(f'Error fetching data: {e}')
        return []

    # pobranie książek przypisanych do gatunku
    results = data.get('works', [])

    # stworzenie formatu pozycji w cache
    if 'genres' not in cache:
        cache['genres'] = {}
    cache['genres'][category] = {'timestamp': now, 'result': results}

    with open(CACHE_FILE, 'wb') as f:
        pickle.dump(cache, f)  # zapisanie pliku cache

    return results

def fetch_cover_image(cover_id, size='M'):
    url = f"https://covers.openlibrary.org/b/id/{cover_id}-{size}.jpg"
    if not cover_id:
        return None
    return url