from rest_framework import serializers

from .models import Movie, Genre, Category
from reviews.serializers import CommentSerializer

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class MoviesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id', 'poster', 'title', 'avarage_rating'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['likes'] = instance.likes.all().count()
        return repr

class MovieDetailSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = Movie
        fields = 'id', 'title', 'description', 'year', 'video', 'genres', 'category', 

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['likes'] = instance.likes.all().count()
        repr['comments'] = CommentSerializer(instance.comments.all(), many=True).data
        return repr

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request')
        if not request.user.is_authenticated:
            fields.pop('video')
        return fields
