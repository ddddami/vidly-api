from rest_framework import serializers
from .models import Genre, Movie


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
