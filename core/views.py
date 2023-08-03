from rest_framework.viewsets import ModelViewSet
from core.models import Genre
from .serializers import GenreSerializer

# Create your views here.
class GenreViewSet(ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()