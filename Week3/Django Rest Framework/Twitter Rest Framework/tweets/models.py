from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
import datetime


class TwitterUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True, default='@NOT_PROVIDED')
    email = models.EmailField('email address', unique=True)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(default=datetime.date.today)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','password']

    def __str__(self):
        return self.username


class Follower(models.Model):
    user = models.ForeignKey(TwitterUser, related_name='twitter_user', on_delete=models.CASCADE)
    followers = models.ForeignKey(TwitterUser, related_name='twitter_followers', on_delete=models.CASCADE)


class Tweet(models.Model):
    tweet = models.CharField(max_length=280)
    user = models.ForeignKey(TwitterUser, related_name='user', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.tweet


# 1  signup / sign in / signout  - Done
# 2. The user can post a tweet. - Done
# 3. User can view profiles of other users. - Done 
# 4. The user can follow other users - Done
# 5. User can search other users - Done (falacy: No login required)
# 6. User can update his profile. e.g name etc - Done

# 7. The user can view tweets or updates set by the users he follows. - ToDo
