from django.urls import path, include
from django.contrib.auth.models import User
from django.contrib.auth.models import models

from rest_framework import viewsets, permissions, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
    
from .models import TwitterUser, Tweet, Follower
from .serializers import TwitterUserSerializer, TweetSerializer, FollowerSerializer


class FollowerView(viewsets.ModelViewSet):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticated]

class TwitterUserView(viewsets.ModelViewSet):
    search_fields = ['username']
    filter_backends = (filters.SearchFilter,)
    queryset = TwitterUser.objects.all()
    serializer_class = TwitterUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        requesting_user = request.user

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        
        if serializer.data[0]['username'] != requesting_user: # to ensure other users cant get see your personal email
            response_data = serializer.data
            del response_data[0]['email']
            return Response(response_data)
        else:
            return Response(serializer.data)

class TweetView(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get_follower_data(self, request):
        queryset = Follower.objects.get_queryset()
        context={'request': request}
        
        return (FollowerSerializer(queryset, many=True, context=context).data)

    def get_users_data(self, request):
        queryset = TwitterUser.objects.get_queryset()
        context={'request': request}
        
        return (TwitterUserSerializer(queryset, many=True, context=context).data)

    def get_user_id(self, username, users):
        for u in users:
            if u[0] == str(username):
                return u[1]
        return False

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        requesting_user = request.user
        
        #print("User : ",requesting_user)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        
        twitter_user_data  = self.get_users_data(request)
        follower_data  = self.get_follower_data(request)
        tweet_data = serializer.data
        
        users=[]
        for u in twitter_user_data: 
            users.append([u['username'], u['id']])
        user_id = self.get_user_id(requesting_user, users)
        
        user_is_a_follower_of = False
        for f in follower_data: 
            if user_id in f['followers']:
                user_is_a_follower_of = f['user']

        response={}
        for t in tweet_data: 
            if user_id == t['user']:
                print("this is the users tweet")
                response.update(t)
            elif user_is_a_follower_of == t['user']:
                print("this tweet is followed by user")
                response.update(t)
        if len(response) != 0:
            return Response(response)
        else:
            return Response("You dont have any tweets, either follow a user or post your own tweet")