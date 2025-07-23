from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    year = models.PositiveIntegerField()
    genres = models.ManyToManyField(Genre)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='movies')
    poster = models.ImageField(upload_to='posters/', blank=True)
    video = models.FileField(upload_to='video/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    avarage_rating = models.FloatField(default=0.0, blank=True)
    is_series = models.BooleanField(default=False, blank=True)

    def save(self, *args, **kwargs):
        if self.category == 'Сериалы':
            self.is_series = True
            self.video = None
        else:
            self.is_series = False
        super().save(*args, **kwargs)

    def update_avarage_rating(self):
        ratings = self.ratings.all()
        if ratings.exists():
            total_score = sum(rating.score for rating in ratings)
            count = len(ratings)
            self.avarage_rating = round(total_score / count, 1)
        else:
            self.avarage_rating = 0.0
        self.save()

    def __str__(self):
        return self.title

class Episode(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='episodes')
    title = models.CharField(max_length=255)
    episode_number = models.PositiveIntegerField()
    video = models.FileField(upload_to='series/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = 'episode_number',

    def __str__(self):
        return f"{self.movie.title} - Серия {self.episode_number}"
