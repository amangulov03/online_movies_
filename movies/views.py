from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter

from django_filters.rest_framework import DjangoFilterBackend


from .models import Movie
from .serializers import MovieSerializer
from .permissions import IsAdminOrCustomer

class MovieModelViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAdminOrCustomer]
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('genres',)
    search_fields = ('title', )
