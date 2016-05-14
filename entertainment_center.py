import fresh_tomatoes
import media
import tmdbsimple as tmdb

tmdb.API_KEY = 'd78bc59d5b627bb60f655fdcafb19dd5'
movies = []
count = 100

movie = tmdb.Movies(101)
response = movie.info()

while count < 110:
    movie = tmdb.Movies(count)
    response = movie.info()
    if (movie.video is False):
        movie.video = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    movies.append(media.Movie(movie.title,movie.overview,"https://image.tmdb.org/t/p/original/"+movie.poster_path,"https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
    count += 1


#toy_story = media.Movie("Toy Story", "Toys come to life", "URL LINK of poster", "YOUTUBE URL")
#avatar = media.Movie("Avatar", "a marine on an alien planet","URL","URL")


#print(toy_story.storyline)
#print(avatar.storyline)
#avatar.show_trailer()




fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
