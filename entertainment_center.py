import fresh_tomatoes
import media
import tmdbsimple as tmdb
import random
import argparse
import re
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

tmdb.API_KEY = 'd78bc59d5b627bb60f655fdcafb19dd5'
movies = []
count = 0

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyDb9YpfOu0mv717uaky5y_QVuGCgNrXRyE"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

videos = []


def youtube_search(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)
    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        q=options.q,
        part="id,snippet",
        maxResults=options.max_results
    ).execute()

    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                       search_result["id"]["videoId"]))

#  print ("Videos:\n", "\n".join(videos), "\n")
#  print(videos[1] + "----------")


movie = tmdb.Movies(100)
response = movie.info()

while count < 3:
        # Grabs a random movie from the database
    movie = tmdb.Movies(random.randint(2, 150))
    response = movie.info()
    # Create a new argparse to refresh arguments to none
    a = argparse.ArgumentParser(description='none')
    # Search using the new movie title trailer
    a.add_argument(
        "--q", help="Search term", default=movie.title + " Trailer")
    # Maximum results defined by default
    a.add_argument("--max-results", help="Max results", default=1)
    args = a.parse_args()
    try:
        youtube_search(args)
    except:
        print("ERROR")
    video_ID = re.findall('\(.*?\)',videos[count]).pop()[1:-1]
    print(video_ID)
    # Add the random movie to our Array of Movies
    movies.append(
        media.Movie(movie.title, movie.overview,
                    "https://image.tmdb.org/t/p/original/" +
                    movie.poster_path,
                    "https://www.youtube.com/watch?v=" + video_ID))
    count += 1
# Open and generate the HTML file of our movies
fresh_tomatoes.open_movies_page(movies)
