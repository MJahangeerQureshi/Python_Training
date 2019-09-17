from datetime import datetime, date, timedelta

from django.conf import settings
from django.contrib.auth.models import User as TwitterUser

from rest_framework import viewsets, permissions, status 
from rest_framework.views import APIView # A default view
from rest_framework.authentication import TokenAuthentication # To setup token Authentication
from rest_framework.response import Response # To send back Http responses
from rest_framework.authtoken.models import Token # To generate a token during signup

from .models import Tweet, Follower
from .serializers import TweetSerializer, FollowerSerializer

def is_token_expired(request):
    """
    Checks to see if token has expired

    The post function creates a new user and assigns it a Token

    Parameters: 
    request : the request from the user 
    format : the format of the request

    Returns: 
    Response (dictionary) : the created user instance
    """
    expiration_duration = timedelta(settings.TOKEN_EXPIRED_AFTER_DAYS)
    token_creation_date = date(request.user.auth_token.created.year,
                            request.user.auth_token.created.month,
                            request.user.auth_token.created.day)
    current_date = date(datetime.now().year,datetime.now().month,datetime.now().day)
                    
    if (current_date - token_creation_date) >= (expiration_duration):
        return True
    else:
        return False

class TweetView(viewsets.ModelViewSet):
    """ 
    An altered View class for Tweets
    with the list method overidden.
    """
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated] 

    lookup_field = 'username' # set the lookup to be the username for ease of use
    
    def create(self, request):
        """
        To prevent creating a new entry via post
        """
        return Response('Only GET here', status=status.HTTP_403_FORBIDDEN)
    
    def update(self, request, *args, **kwargs):                            
        """
        To prevent creating a new entry via put/patch
        """
        return Response('Only GET here', status=status.HTTP_403_FORBIDDEN)
    
    def response_based_on_currentuser(self, serializer, request):
        """
        Formulates a response based on the requesting user

        This function allows us to show a user only their tweets
        and the tweets of the people they follow

        Parameters: 
        serializer : the model serializer for tweets
        request : the request from the user 
  
        Returns: 
        Response (list) : A list of tweets 
        """
        followers = Follower.objects.all()
        requesting_user = str(request.user)
        response = []

        for tweet in serializer.data:
            if tweet['username'] == requesting_user: 
                response.append(tweet)                  # if the tweet belongs to the user pass it through
            else:
                for followee in followers:
                    if str(followee.followers) == requesting_user and tweet['username'] == str(followee.user):
                        response.append(tweet)          # if the tweet belongs to a user whom the current user follows    
                                                        # pass it through
        return response

    def list(self, request):
        """
        Lists all tweets

        This function allows us to list the tweets selectivly by showing a user only their tweets
        and the tweets of the people they follow

        Parameters: 
        request : the request from the user 
  
        Returns: 
        Response (list) : A list of tweets 
        """
        if is_token_expired(request):
            request.user.auth_token.delete()
            return Response("Your session has expired you will need to login again")
        else:
            serializer = self.get_serializer(self.get_queryset(), many=True)
            return Response(self.response_based_on_currentuser(serializer, request))
    
    def retrieve(self, request, username):
        """
        Lists a tweet

        This function allows us to show a tweet selectivly by showing a user only their tweet
        and the tweet of the person they follow

        Parameters: 
        request : the request from the user 
        username : lookupfield for tweets
  
        Returns: 
        Response (list) : A list of tweets 
        """
        if is_token_expired(request):
            request.user.auth_token.delete()
            return Response("Your session has expired you will need to login again")
        else:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(self.response_based_on_currentuser(serializer, request))


class CreateTweet(APIView):
    """ 
    A Create class for Tweets
    with the list method overidden.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format='json'):
        """
        posts a tweet

        This function allows us to show post a tweet and prepopulate the user fields based on
        the user making the request

        Parameters: 
        request : the request from the user 
        format : format for the request data
  
        Returns: 
        Response (list) : The Posted Tweet 
        """
        if is_token_expired(request):
            request.user.auth_token.delete()
            return Response("Your session has expired you will need to login again")
        else:
            try:
                serializer_data = {
                    "user":request.user.id,
                    "username":str(request.user),    # add user and username based on info from request
                    "tweet":request.data['tweet']
                }
                serializer = TweetSerializer(data=serializer_data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(serializer.errors)
            except KeyError:
                return Response('System_Message : Please pass the tweet you wish to post')

class CreateFollower(APIView):
    """ 
    An Create class for Tweets
    with the list method overidden.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def check_if_already_following(self, request, user_model):
        """
        Checks if a user is already following another user

        This function checks if the requesting user already follows the user they are trying to follow.

        Parameters: 
        request : the request from the user 
        user_model : a User instance
  
        Returns: 
        Boolean : returns True if already following and false if otherwise 
        """
        followees = Follower.objects.all()
        for follow in followees:
            if str(request.user.username) == str(follow.followers) and str(user_model.username) == str(follow.user):
                return True
        return False

    def post(self, request, format='json'):
        """
        Creates a followee

        This function allows a user to follow another user by passing their username. 
        A follower instance is then created where the "follower" is the user making the request
        and the "user" is the user the requesting user is trying to follow

        Parameters: 
        request : the request from the user 
        format : format for the request data
   
        Returns: 
        Response : the created follower instance 
        """
        if is_token_expired(request):
            request.user.auth_token.delete()
            return Response("Your session has expired you will need to login again")
        else:
            users_model = TwitterUser.objects.all()
            for user_model in users_model:
                try:
                    if str(user_model.username) == request.data['follow']:
                        if self.check_if_already_following(request, user_model): # if already following pass this message
                            return Response('System_Message : You are already following this User')        
                        else:                                                    # pass the new follower instance
                            serializer_data = {                                  
                                    "user":user_model.id,
                                    "username":request.data['follow'], 
                                    "followers":request.user.id,        # add follower name based on info from request
                                    "followername":str(request.user),
                                }
                            serializer = FollowerSerializer(data=serializer_data)
                            if serializer.is_valid():
                                print('serializer is valid')
                                serializer.save()
                                return Response(serializer.data, status=status.HTTP_201_CREATED)
                            else:
                                return Response(serializer.errors)
                except KeyError:
                    return Response('System_Message : Please pass the follower names')
                
            return Response('System_Message : No user with such a username exists')
