import fresh_tomato
import webbrowser


# Here I make a class name 'Movies' which can read all
# the data of movies like 'avenger'. To read the data
# I write class name before the '()' in every movie data.

class Movie():
    # here in the below fuction __init__ create
    # a space or memory for the movies.
    def __init__(self, movie_title, poster_image,
                 youtube_trailer):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer

# open youtube trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

# Create movie Avengers using Title, Poster URL and Trailer URL
avengers = Movie("The Avengers",
                 "https://bit.ly/1N3f5G7",
                 "https://www.youtube.com/watch?v=eOrNdBpGMv8")

# Create movie Now You See Me using Title, Poster URL and Trailer URL
now_you_see_me = Movie("Now You See Me",
                       "https://bit.ly/2aQUPC2",
                       "https://www.youtube.com/watch?v=KzJNYYkkhzc")

# Create movie Minions using Title, Poster URL and Trailer URL
minions = Movie("Minions",
                "https://bit.ly/2tXSevY",
                "https://www.youtube.com/watch?v=eisKxhjBnZ0")

# Create movie Johnny English Strike Again
# using Title, Poster URL and Trailer URL
johnny_english_strikes_again = Movie("Johnny English Strikes Again",
                                     "https://bit.ly/2HeeYAo",
                                     "https://bit.ly/2GWWdRr")

# Create movie Kingsman using Title, Poster URL and Trailer URL
kingsman = Movie("Kingsman: The Secret Service",
                 "https://bit.ly/2XTrKJE",
                 "https://www.youtube.com/watch?v=kl8F-8tR8to")

# Create movie Deadpool using Title, Poster URL and Trailer URL
deadpool = Movie("Deadpool",
                 "https://bit.ly/2UtsseB",
                 "https://www.youtube.com/watch?v=Xithigfg7dA")

# List of movies that will be shown in page
movies = [avengers, now_you_see_me, minions,
          johnny_english_strikes_again, kingsman, deadpool]

# Create movies pages
fresh_tomato.open_movies_page(movies)
