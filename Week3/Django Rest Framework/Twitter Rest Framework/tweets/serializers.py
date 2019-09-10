from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer

import datetime

from .models import TwitterUser, Tweet, Follower


class TweetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tweet
        fields = ('id', 'url', 'tweet', 'user')


class FollowerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Follower
        fields = ('id', 'url', 'user', 'followers')


class TwitterUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TwitterUser
        fields = ('id', 'url', 'username', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = TwitterUser(**validated_data)
        user.set_password(password)
        user.save()

        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        return instance

class RegistrationSerializer(RegisterSerializer):
    name = serializers.CharField(required=True)
    date_of_birth = serializers.DateField(default=datetime.date.today)

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'name': self.validated_data.get('name', ''),
            'email': self.validated_data.get('email', ''),
            'date_of_birth':self.validated_data.get('date_of_birth',''),
            'password1': self.validated_data.get('password1', ''),
            
        }