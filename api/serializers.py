from rest_framework import serializers
from .models import course,rating
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required':True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class courseSerializer(serializers.ModelSerializer):
    class Meta:
        model = course
        fields = ('id', 'title', 'description', 'no_of_ratings', 'avg_ratings')


class ratingSerializer(serializers.ModelSerializer):
    class Meta:
        model = rating
        fields = ('id', 'Course', 'user', 'stars')
