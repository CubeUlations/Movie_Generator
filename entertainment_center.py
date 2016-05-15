import fresh_tomatoes
import media
import tmdbsimple as tmdb
import random
tmdb.API_KEY = 'd78bc59d5b627bb60f655fdcafb19dd5'
movies = []
count = 0

movie = tmdb.Movies(100)
response = movie.info()

while count < 5:
    movie = tmdb.Movies(random.randint(2, 150))
    response = movie.info()
    if (movie.video is False):
        movie.video = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    movies.append(
        media.Movie(movie.title, movie.overview,
                    "https://image.tmdb.org/t/p/original/" +
                    movie.poster_path, movie.video))
    count += 1

fresh_tomatoes.open_movies_page(movies)
