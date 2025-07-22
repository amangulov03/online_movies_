from rest_framework.serializers import ModelSerializer

from .models import Comment, Favorite 

class CommentSerializer(ModelSerializer):
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
    
class FavoriteSerializer(ModelSerializer):
    class Meta:
        model = Favorite
        exclude = ('user', )

    def validate(self, attrs):
        super().validate(attrs)
        attrs['user'] = self.context['request'].user
        return attrs
    
    def to_representation(self, instance):
        from movies.serializers import MoviesListSerializer
        repr = super().to_representation(instance)
        repr['movies'] = MoviesListSerializer(instance.movies).data
        return repr 
    