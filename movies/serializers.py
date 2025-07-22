from rest_framework import serializers

from .models import Movie, Genre, Category

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

class MovieDetailSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = Movie
        fields = '__all__'

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request')
        if not request.user.is_authenticated:
            fields.pop('video')
        return fields
