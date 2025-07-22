from django.db import models
from django.contrib.auth import get_user_model

from movies.models import Movie

User = get_user_model()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    movies = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    movies = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='likes')

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    movies = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='favorites')
