from rest_framework import serializers

from .models import Comment, Favorite

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ('user', )

    def validate(self, attrs):
        super().validate(attrs)
        attrs['user'] = self.context['request'].user
        return attrs

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['user'] = {
            'id':instance.user.id,
            'email':instance.user.email
        }
        repr['movies'] = {
            'id':instance.movies.id,
            'title':instance.movies.title
        }
        return repr

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        exclude = ('user', )

    def validate(self, attrs):
        super().validate(attrs)
        attrs['user'] = self.context['request'].user
        if self.context['request'].method == 'POST':
            if Favorite.objects.filter(user=attrs['user'], movies=attrs['movies']).exists():
                raise serializers.ValidationError("Этот фильм уже в избранном.")
        return attrs

    def to_representation(self, instance):
        from movies.serializers import MovieDetailSerializer
        repr = super().to_representation(instance)
        repr['movies'] = MovieDetailSerializer(instance.movies, context=self.context).data
        return repr
