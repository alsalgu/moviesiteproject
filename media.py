import webbrowser


# Create Movie class to assign information about the movies
class Movie():
    # Define the variables for the movies
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Bring up the movie's trailer in default browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
