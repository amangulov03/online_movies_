from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter

from django_filters.rest_framework import DjangoFilterBackend


from .models import Movie
from .serializers import MovieDetailSerializer, MoviesListSerializer
from .permissions import IsAdminOrCustomer

class MovieModelViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    permission_classes = [IsAdminOrCustomer]
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('genres', 'category', 'avarage_rating')
    search_fields = ('title', )

    def get_serializer_class(self):
        if self.action == 'list':
            return MoviesListSerializer
        return MovieDetailSerializer
