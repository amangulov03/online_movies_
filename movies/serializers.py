from rest_framework import serializers

from .models import Movie, Genre, Category, Episode
from reviews.serializers import CommentSerializer

class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = 'id', 'title', 'episode_number', 'video', 'created_at'

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
    episodes = EpisodeSerializer(many=True)

    class Meta:
        model = Movie
        fields = 'id', 'title', 'description', 'year', 'video', 'episodes', 'genres', 'category',

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['likes'] = instance.likes.all().count()
        repr['comments'] = CommentSerializer(instance.comments.all(), many=True).data
        if not instance.is_series:
            repr.pop('episodes')
        else:
            repr.pop('video')
        return repr

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request')
        if not request.user.is_authenticated:
            fields.pop('video')
            if 'episodes' in fields:
                fields['episodes'].child.fields.pop('video')
        return fields
