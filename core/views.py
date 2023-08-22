from rest_framework.viewsets import ModelViewSet
from core.models import Genre, Movie
from .serializers import GenreSerializer, MovieSerializer

# Create your views here.
class GenreViewSet(ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
class MovieViewSet(ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()