from django.contrib import admin

from .models import Movie, Genre, Category

@admin.register(Movie)
class MoviesAdmin(admin.ModelAdmin):
    filter_horizontal = ('genres',)

admin.site.register(Genre)
admin.site.register(Category)
