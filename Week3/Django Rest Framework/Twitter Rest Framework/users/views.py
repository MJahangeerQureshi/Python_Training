import json
from datetime import datetime, date, timedelta

import django
from django.conf import settings
from django.contrib.auth.models import User as TwitterUser # Our user model
from django.contrib.auth.hashers import check_password # to check the user plaintext password against the users hashed
                                                       # password
from rest_framework import viewsets, permissions, status 
from rest_framework.views import APIView # A default view
from rest_framework.authentication import TokenAuthentication # To setup token Authentication
from rest_framework.response import Response # To send back Http responses
from rest_framework.authtoken.models import Token # To generate a token during signup

from .serializers import TwitterUserSerializer, TwitterUserSerializerForUsers

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


class UserView(viewsets.ModelViewSet):
    """ 
    An altered View class for User
    with the list and the retrieve method overidden
    to allow for minimal privacy
    """
    queryset = TwitterUser.objects.all()
    serializer_class = TwitterUserSerializerForUsers
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    lookup_field = 'username' #** Set the username as the lookup value in the URL

    def list(self, request):  
        """
        Returns a list of all existing Users

        The list function takes into account the user making the request
        and edits the list to obscure private details such as the email

        Parameters: 
        request : the request from the user 
  
        Returns: 
        Response (list) : A list of all the users 
        """
        if is_token_expired(request):
            request.user.auth_token.delete()
            return Response("Your session has expired you will need to login again")
        else:
            serializer = self.get_serializer(self.queryset, many=True)
            response = []
            for user in serializer.data:
                if str(request.user) == user['username']: # Check if the user is the requesting user
                    response.append({
                        "username":user['username'],      # if yes, add email
                        "email":user['email']
                    })
                else:
                    response.append({
                        "username":user['username']       # if no, ignore email
                    })
            return Response(response)
    
    def retrieve(self, request, username):
        """
        Returns an instance of an existing Users

        The retrieve function takes into account the user making the request
        and edits the list to obscure private details such as the email

        Parameters: 
        request : the request from the user 
  
        Returns: 
        Response (dictionary) : the requested user instance
        """
        if is_token_expired(request):
            request.user.auth_token.delete()
            return Response("Your session has expired you will need to login again")
        else:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            user = serializer.data

            if username == user['username']:              # Check if the user is the requesting user
                response = { "username":user['username'],
                                "email":user['email']     # if yes, add email
                                }
            else:
                response = {"username":user['username']}  # if no, ignore email

            return Response(response)

class UserCreate(APIView):
    """ 
    Creates the user/ The Signup class. 
    Accounts for the following edge cases when creating a new user:
        - Username already exists
        - Username not provided
        - Username too long
        - Password not provided
        - Password too short
        - Email already taken
        - Email not provided
        - Invalid email format
    """

    def post(self, request, format='json'):
        """
        Creates a new User instance

        The post function creates a new user and assigns it a Token

        Parameters: 
        request : the request from the user 
        format : the format of the request

        Returns: 
        Response (dictionary) : the created user instance
        """
        serializer = TwitterUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user) # Creating a new token for the user
                data = serializer.data                  # essentially signing him in
                data['token'] = token.key
                print(token.key)
                return Response(data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

class Login(APIView):
    """ 
    Returns the users token/The Signin class. 
    """
    def user_has_key(self, user_model): # checks to see if a user has a token
        """
        Checks the user has a token 

        If the user hasd a token he is essentially signed in 

        Parameters: 
        user_model : the user instance we wish to check

        Returns:
        If token exists: 
            Token : the user instance token
        If token does not exist:
            False : to signify the user is not signed in 
        """
        try:
            return user_model.auth_token
        except django.contrib.auth.models.User.auth_token.RelatedObjectDoesNotExist:
            return False
    
    def post(self, request):
        """
        Logins the User

        References the username and password and creates a token if
        the they match

        Parameters: 
        request : the user request

        Returns:
        Response (dictionary) : Returns Username, Email and Token
        """
        post_data = json.loads(request.body)
        
        for user_model in TwitterUser.objects.all():
            try:
                if post_data['username'] == user_model.username and check_password(post_data['password'], user_model.password):
                    user_key = self.user_has_key(user_model) # checks to see if a user has a token
                    if user_key:                             # if the user has a key this response is sent 
                        response = {
                            "System_Message":"You were already logged in",
                            "Username":user_model.username,
                            "Email":user_model.email,
                            "Token":str(user_key)
                            }
                        return Response(response, status=status.HTTP_200_OK)
                    else: 
                        token = Token.objects.create(user=user_model) # if the user doesnt have a key 
                                                                      # a new key is generated
                        
                        response = {
                            "Username":user_model.username,
                            "Email":user_model.email,
                            "Token":token.key
                            }
                        return Response(response, status=status.HTTP_200_OK)
            except KeyError:
                return Response('Login failed, please ensure username or password has been passed')
                
        return Response('Login failed, please ensure username or password is correct')

class LogoutAllUsers(APIView):
    """ 
    Deletes the tokens of all users
    usefull for testing the signup, login and logout methods 
    """ 
    permission_classes = [permissions.IsAdminUser] # Only meant to be used by the admin

    def post(self, request):
        """
        Logouts all Users

        Deletes all user tokens

        Parameters: 
        request : the user request

        Returns:
        Response (string) :  A system message
        """
        for user_model in TwitterUser.objects.all():
            try:
                user_model.auth_token.delete()     # If a key exists delete it
            except django.contrib.auth.models.User.auth_token.RelatedObjectDoesNotExist:
                pass                               # If a key does not exist, ignore and pass
        return Response("All users have been logged out")

class Logout(APIView):
    """ 
    Returns the users logs the user out. 
    """
    def post(self, request):
        """
        Logouts a User

        Deletes a user token based on the username

        Parameters: 
        request : the user request

        Returns:
        Response (string) :  A system message
        """
        post_data = json.loads(request.body)
        
        for user_model in TwitterUser.objects.all():
            try: 
                if post_data['username'] == str(user_model):
                    try:
                        user_model.auth_token.delete() 
                        return Response("System_Message : You have been logged out") # If a key exists delete it
                    except django.contrib.auth.models.User.auth_token.RelatedObjectDoesNotExist:
                        return Response("System_Message : You are already logged out") # If a key does not exist, ignore and pass
            except KeyError:
                return Response("System_Message : Please enter the username field")        
        return Response("System_Message : No such user")