from django.db import models

from django.contrib.auth.models import User


# Create your models here.
class RatedMovies(models.Model):
    movie_id = models.CharField(max_length=254)
    movie_title = models.TextField(default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.id+self.movie.name


