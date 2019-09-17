from django.db import models
from django.contrib.auth.models import User as TwitterUser
 
class Tweet(models.Model):
    """
    This a class for the Follower model
    it declare the following fields.

    tweet : A CharField with a max length of 280 characters.
    username : A CharField with a max length of 280 characters set to be unique
    user : A ForeignKey to the twitter user model.
    """
    tweet = models.CharField(max_length=280)
    username = models.CharField(max_length=150, unique=True, null=True) # to make viewing a tweet somewhat intuitive
    user = models.ForeignKey(TwitterUser, related_name='user', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.tweet

class Follower(models.Model):
    """
    This a class for the Follower model
    it declare the following fields.

    user : A ForeignKey to the twitter user model.
    followers : A ManyToManyField with the twitter user model.
    """
    username = models.CharField(max_length=150, null=True)      # to make viewing a follower 
    followername = models.CharField(max_length=150, null=True)  # somewhat intuitive
     

    user = models.ForeignKey(TwitterUser, related_name='twitter_user', on_delete=models.CASCADE, null=True)
    followers = models.ForeignKey(TwitterUser, related_name='twitter_followers', on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.username

