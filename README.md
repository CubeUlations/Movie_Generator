# Movie_Generator
Generates a set of movies from the TMDB API. Displays the movie in a website. When clicked a video of that movie shows up.

<b> Code Instructions </b> <br />
<b> movie = tmdb.Movies(NUMBER) </b> , NUMBER = The Unique ID of the movie <br />
<b> response = movie.info() </b>, This must be called (Directly after a Unique ID Call) so the functions below will work <br />
<b> movie.DATA </b>, DATA = The specific information from the movie. <br />
Examples: movie.title (Title of Movie), movie.overview (Summary of Movie) <br />

<b> API LINK: </b>
https://github.com/celiao/tmdbsimple

<b> API Instructions </b> <br />
1) Install the API, <br />
pip install tmdbsimple <br />
2) Get an API key, <br />
https://www.themoviedb.org/?_dc=1463284008 <br />
3) Start coding!
