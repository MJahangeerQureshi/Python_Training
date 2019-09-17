from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tweets', views.TweetView)

urlpatterns = [
    path('', include(router.urls)),
    path('post-tweet', views.CreateTweet.as_view(), name='Create-Tweet'), # create a new tweet
    path('follow-user', views.CreateFollower.as_view(), name='Follow-User') # follow a user using their username
]

