from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tweets', views.TweetView)
router.register('users', views.TwitterUserView)
router.register('followers ', views.FollowerView)

urlpatterns = [
    path('', include(router.urls))
]
