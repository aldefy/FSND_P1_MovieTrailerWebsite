import media
import fresh_tomatoes

leon_the_professional = media.Movie("Lieon: The Professional", "Mathilda, a 12-year-old girl, is reluctantly taken in by Lieon, a professional assassin, after her family is murdered. Lieon and Mathilda form an unusual relationship, as she becomes his protiegiee and learns the assassin's trade.", "http://ia.media-imdb.com/images/M/MV5BMTgzMzg4MDkwNF5BMl5BanBnXkFtZTcwODAwNDg3OA@@._V1_SY317_CR4,0,214,317_AL_.jpg", "https://www.youtube.com/watch?v=DcsirofJrlM")
avatar = media.Movie("Avatar", "A Paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home..", "http://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_SY317_CR0,0,214,317_AL_.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")

movies = [leon_the_professional, avatar]
fresh_tomatoes.open_movies_page(movies)

print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)