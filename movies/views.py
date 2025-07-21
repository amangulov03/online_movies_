from rest_framework.viewsets import ModelViewSet

from .models import Movie
from .serializers import MovieSerializer

class MovieModelViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    