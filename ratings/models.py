from django.db import models
from django.contrib.auth import get_user_model
from movies.models import Movie

User = get_user_model()

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    score = models.PositiveIntegerField()

    class Meta:
        unique_together = 'user', 'movie'

    def __str__(self):
        return f"{self.user.username} - {self.movie.title}: {self.score}"
