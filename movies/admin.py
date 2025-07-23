from django.contrib import admin

from .models import Movie, Genre, Category, Episode

@admin.register(Movie)
class MoviesAdmin(admin.ModelAdmin):
    filter_horizontal = ('genres',)

admin.site.register(Genre)
admin.site.register(Category)
admin.site.register(Episode)
