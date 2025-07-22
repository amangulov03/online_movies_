from rest_framework import serializers

from .models import Rating

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        exclude = ('user', )

    def validate_score(self, value):
        if 1 <= value <= 5:
            return value
        raise serializers.ValidationError('Оценка должна быть от 1 до 5.')

    def validate(self, attrs):
        super().validate(attrs)
        attrs['user'] = self.context['request'].user
        return attrs

    def create(self, validated_data):
        user = validated_data['user']
        movie = validated_data['movie']
        score = validated_data['score']

        rating, created = Rating.objects.get_or_create(
            user=user,
            movie=movie,
            defaults={'score': score}
        )
        if not created:
            rating.score = score
            rating.save()

        rating.movie.update_avarage_rating()
        return rating
