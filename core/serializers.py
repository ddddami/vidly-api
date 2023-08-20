from rest_framework import serializers
from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer
from djoser.conf import settings
from .models import Genre, Movie
from django.contrib.auth import get_user_model
from djoser.conf import settings

User = get_user_model()


class UserSerializer(BaseUserSerializer):
    isAdmin = serializers.BooleanField(source='is_staff', read_only=True)
    name = serializers.CharField(source='first_name')

    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username',
                  'name', 'isAdmin']


class UserCreateSerializer(UserCreateSerializer):
    name = serializers.CharField(source='first_name')

    class Meta(UserCreateSerializer.Meta):
        fields = ('username', 'password', 'name',)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['_id', 'name']


class MovieSerializer(serializers.ModelSerializer):
    numberInStock = serializers.IntegerField(source='number_in_stock')
    dailyRentalRate = serializers.DecimalField(
        decimal_places=1, max_digits=2, source='daily_rental_rate')
    genre = GenreSerializer(read_only=True)
    genreId = serializers.CharField(source='genre_id')

    class Meta:
        model = Movie
        fields = ['_id', 'title', 'genre',
                  'numberInStock', 'dailyRentalRate', 'genreId']

    # def update(self, instance, validated_data):
    #     genre_id = validated_data.pop('genre_id')
    #     genre = Genre.objects.get(pk=genre_id)
    #     instance.genre = genre
    #     super().update(instance, validated_data)
    #     return instance
