from rest_framework import serializers
from .models import Tweet, Follower

class TweetSerializer(serializers.ModelSerializer):
    """
    This a class for the tweet serializer, it inherits
    for the serializers.ModelSerializer
    """
    class Meta:
        model = Tweet
        fields = ('id', 'user', 'username','tweet')


class FollowerSerializer(serializers.ModelSerializer):
    """
    This a class for the follower serializer, it inherits
    for the serializers.ModelSerializer
    """
    class Meta:
        model = Follower
        fields = ('id', 'user','followers','username', 'followername')