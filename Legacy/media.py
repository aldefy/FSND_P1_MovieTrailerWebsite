import webbrowser


class Video():

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def show_info(self):
        print(self.title + " " + self.duration)


class Movie(Video):
    """This class provides a way to store movie related information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # constructor
    def __init__(self, title, duration, storyline, poster_image_url, trailer_youtube_url):
        Video.__init__(self, title, duration)
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
