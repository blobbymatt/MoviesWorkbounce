from rest_framework import serializers
from movies.models import RatedMovies
from rest_framework import serializers
from django.contrib.auth import get_user_model

class RateMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model= RatedMovies
        fields=['rating', 'movie_id', 'movie_title' ]

    def create(self, validated_data):
        request = self.context.get('request', None)
        if request:
            if RatedMovies.objects.filter(movie_id=validated_data['movie_id'],
                                       movie_title=validated_data['movie_title'],
                                       user=request.user).exists():
                this_rating = RatedMovies.objects.get(movie_id=validated_data['movie_id'],
                                                      movie_title=validated_data['movie_title'],
                                                      user=request.user)
                this_rating.rating = validated_data['rating']
                this_rating.save()
            else:
                this_rating = RatedMovies(movie_id=validated_data['movie_id'],
                                          movie_title=validated_data['movie_title'],
                                          user=request.user,
                                          rating=validated_data['rating'])
                this_rating.save()

            return this_rating


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'password',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super(UserSerializer, self).update(instance, validated_data)