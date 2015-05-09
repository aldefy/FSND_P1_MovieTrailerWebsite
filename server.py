from fresh_tomatoes import open_movies_page

class Movie:
  """Store movie related infromation"""
  def __init__(self, title, poster_url, trailer_url):
    self.title = title
    self.poster_image_url = poster_url
    self.trailer_youtube_url = trailer_url


# movies title list
movies_title = ["The Shawshank", "The Godfather", "The Godfather: Part II", "The Dark Knight", "Pulp Fiction", "Schindler's List"]

# movies poster url list
movies_poster = ["http://ia.media-imdb.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_SX214_AL_.jpg","http://ia.media-imdb.com/images/M/MV5BMjEyMjcyNDI4MF5BMl5BanBnXkFtZTcwMDA5Mzg3OA@@._V1_SX214_AL_.jpg","http://ia.media-imdb.com/images/M/MV5BNDc2NTM3MzU1Nl5BMl5BanBnXkFtZTcwMTA5Mzg3OA@@._V1_SX214_AL_.jpg","http://ia.media-imdb.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY317_CR0,0,214,317_AL_.jpg","http://ia.media-imdb.com/images/M/MV5BMjE0ODk2NjczOV5BMl5BanBnXkFtZTYwNDQ0NDg4._V1_SY317_CR4,0,214,317_AL_.jpg", "http://ia.media-imdb.com/images/M/MV5BMzMwMTM4MDU2N15BMl5BanBnXkFtZTgwMzQ0MjMxMDE@._V1_SX214_AL_.jpg"]

# movies trailer url list
movies_trailer = ["https://www.youtube.com/watch?v=6hB3S9bIaco", "https://www.youtube.com/watch?v=sY1S34973zA", "https://www.youtube.com/watch?gl=SG&hl=en-GB&v=qJr92K_hKl0", "https://www.youtube.com/watch?v=EXeTwQWrcwY", "https://www.youtube.com/watch?v=s7EdQ4FqbhY","https://www.youtube.com/watch?v=dwfIf1WMhgc"]

movies = []

for i in range(0, 6):
  movie = Movie(movies_title[i], movies_poster[i], movies_trailer[i])
  movies.append(movie)

open_movies_page(movies)