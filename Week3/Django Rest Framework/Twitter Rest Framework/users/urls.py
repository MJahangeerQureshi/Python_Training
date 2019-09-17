from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register('users', views.UserView)

urlpatterns = [
    path('', include(router.urls)), 
    path('signup', views.UserCreate.as_view(), name='Signup'), # creates a user instance and assigns it a token   
    path('login', views.Login.as_view(), name='Login'), # creates a token if one doesnt exist and returns it
    path('logout', views.Logout.as_view(), name='Logout'), # delete a token if one doesnt exist
    path('logoutall', views.LogoutAllUsers.as_view(), name='Logout-All-Users'), # deletes all tokens (admin only)
]