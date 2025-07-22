from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from movies.models import Movie

from .models import Comment, Like, Favorite
from .serializers import CommentSerializer, FavoriteSerializer

class CommentModelViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class FavoriteModelViewSet(ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [ IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
@api_view(['POST'])
def toogle_like(request, id):
    user = request.user
    if not user.is_authenticated:
        return Response(status=401)
    movies = get_object_or_404(Movie, id=id)
    if Like.objects.filter(user=user, movies=movies).exists():
        Like.objects.filter(user=user, movies=movies).delete()
    else:
        Like.objects.create(user=user, movies=movies)
        return Response(status=201)
    