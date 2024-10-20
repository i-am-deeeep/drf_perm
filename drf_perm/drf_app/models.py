from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=50)
    storyline=models.CharField(max_length=200)
    budget_INR=models.IntegerField()
    profitable=models.BooleanField()
    released_date=models.DateField()
    avg_rating=models.FloatField(default=0)
    num_of_ratings=models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Review(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    rating=models.IntegerField()
    description=models.CharField(max_length=200)
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)+" | "+self.movie.title