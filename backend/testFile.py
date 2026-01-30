import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from apps.books.books_additional_files.genresMatrix import subject_to_keywords
import os
import pickle
import time
import json



# # CACHE_FILE = 'cache_books.pkl'  # nazwa pliku
# # EXPIRATION_SECONDS = 7 * 24 * 60 * 60  # ilość czasu, jaką jest pozycja w cache


# # #  załadowanie cache, jeśli jest
# # if os.path.exists(CACHE_FILE):
# #     with open(CACHE_FILE, 'rb') as f:
# #         cache = pickle.load(f)

# # else:
# #     cache = {}


# def fetch_best_book_category(title):
#     # now = time.time()  # aktualny timestamp (sekundy od 1970)
#     # zmiana tytułu na małe litery bez spacji na początku i końcu
#     title = title.lower().strip()

#     # # sprawdzenie, czy pozycja jest już w cache, słownik w słowniku
#     # if 'titles' in cache and title in cache['titles']:
#     #     entry = cache['titles'][title]  # przypisanie do zmiennej

#     #     # sprawdzenie czy mieści się w zakresie czasowym
#     #     if now - entry['timestamp'] < EXPIRATION_SECONDS:
#     #         return entry['result']  # zwrócenie pozycji z cache

#     # przygotowanie tytułu i wyszukanie w API
#     title_query = title.replace(' ', '_')
#     url = f"https://openlibrary.org/subjects/{title_query}.json"

#     try:
#         response = requests.get(url)
#         response.raise_for_status()  # w przypadku błędu będzie HTTPError
#         data = response.json()
#     except Exception as e:
#         print(f'Error fetching data: {e}')
#         return []

#     subjects = [' '.join(work.get('subject', []))
#                 for work in data.get('works', [])]  # pobranie gatunków przypisanych do książki

#     # stworzenie formatu pozycji w cache
#     # if 'titles' not in cache:
#     #     cache['titles'] = {}
#     # cache['titles'][title] = {'timestamp': now, 'result': subjects}

#     # with open(CACHE_FILE, 'wb') as f:
#     #     pickle.dump(cache, f)  # zapisanie pozycji do cache

#     return subjects  # zwracam gatunki


# def fetch_books_by_category(subject):
#     now = time.time()  # aktualny timestamp (sekundy od 1970)
#     # zmiana tytułu na małe litery
#     subject = subject.lower()

#     # # sprawdzenie, czy jest już taki słownik i podsłowniki z żądanym gatunkiem
#     # if 'genres' in cache and subject in cache['genres']:
#     #     entry = cache['genres'][subject]  # przypisanie zmiennej
#     #     if now - entry['timestamp'] < EXPIRATION_SECONDS:

#     #         return entry['result']  # zwrócenie pozycji, jeśli jest

#     url = f"https://openlibrary.org/subjects/{subject}.json"

#     try:
#         response = requests.get(url)
#         response.raise_for_status()  # w przypadku błędu będzie HTTPError
#         data = response.json()
#     except Exception as e:
#         print(f'Error fetching data: {e}')
#         return []

#     # pobranie książek przypisanych do gatunku
#     titles = [work.get('title', '') for work in data.get('works', [])]

#     # # stworzenie formatu pozycji w cache
#     # if 'genres' not in cache:
#     #     cache['genres'] = {}
#     # cache['genres'][subject] = {'timestamp': now, 'result': titles}

#     # with open(CACHE_FILE, 'wb') as f:
#     #     pickle.dump(cache, f)  # zapisanie pliku cache

#     return titles


# title = "lord of the rings"

# subjects = fetch_best_book_category(title)



# title_stop = title.lower().split()  # przygotowanie tytułu jako stop word

# custom_stop_words = ['english', 'en', 'literature', 'novel', 'criticism',
#                          'motion', 'picture', 'pictures', 'film', 'video',
#                          'adaptation', 'adaptations', 'films', 'movie', 'movies',
#                          'cinema', 'dvd', 'blu-ray', 'edition', 'collection',
#                          'game', 'games', 'videogames', 'playstation', 'xbox',
#                          'general', 'fiction', 'works', 'pictorial', 'illustrations',
#                          'study', 'criticism', 'analysis', 'companion', 'guide',
#                          'book', 'books', 'reading', 'library'] + title_stop  # stworzenie listy stop words

# stop_words = list(ENGLISH_STOP_WORDS) + (custom_stop_words)

# # tworzenie obiektu dla wektora
# vectorizer = TfidfVectorizer(stop_words=stop_words, max_df=0.8, min_df=2)
# # trenowanie i przekształcanie gatunków w matrycę
# tfidf_matrix = vectorizer.fit_transform(subjects)

# # przypisanie nazwy kolumn do zmiennej
# feature_names = vectorizer.get_feature_names_out()

# # podsumowanie wyników dla każdej kolumny
# word_scores = tfidf_matrix.mean(axis=0).A1
# # pobranie najbardziej pasującego gatunku dla książki

# # do zmiany, 3 gatunki, na 1 są błędy
# '''best_word = feature_names[word_scores.argmax()]'''

# top_n = 5  # ile top słów

# top_indices = word_scores.argsort()[::-1][:top_n] # indeksy słów posortowane rosnąco

# best_words = [feature_names[i]for i in top_indices]

# print(best_words)

# for word in best_words:
#     print(fetch_books_by_category(word)[:3])
#     print('-----------------')


# '''for book in best_book[:20]:
#     print(book)
#     print("---------")'''


url = "https://openlibrary.org/search.json?title=the+lord+of+the+rings&limit=1"

try:
    response = requests.get(url)
    response.raise_for_status()  # w przypadku błędu będzie HTTPError
    data = response.json()
    
    data = data.get("docs")
    
    for book in data:
        work_key = book.get("key")
        
        response = requests.get(f"https://openlibrary.org{work_key}.json")
        response.raise_for_status()
        result = response.json()
        
        subjects = result.get("subjects")
        
        print(subjects[:10])
        
except Exception as e:
    print(f'Error fetching data: {e}')