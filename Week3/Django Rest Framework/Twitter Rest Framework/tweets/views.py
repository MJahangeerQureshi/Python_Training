from django.urls import path, include
from django.contrib.auth.models import User

from rest_framework import viewsets, permissions, filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
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
    
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        requesting_user = request.user
        
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        print(serializer.data[0])
        return Response(serializer.data)
        
