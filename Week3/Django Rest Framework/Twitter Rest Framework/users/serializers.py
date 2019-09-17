from rest_framework import serializers
from rest_framework.validators import UniqueValidator # to verify if a field is unique
from django.contrib.auth.models import User as TwitterUser # used to augment default User model for our needs

class TwitterUserSerializer(serializers.ModelSerializer):
    """
    This class for the users serializer is meant to be used during signup only.
    This is in the intrests of privacy, to prevent other users from viewing a users
    private info such as his email and password
    """
    username = serializers.CharField(max_length=30,
                                    validators=[UniqueValidator(queryset=TwitterUser.objects.all())])

    email = serializers.EmailField(required=True,
                                    validators=[UniqueValidator(queryset=TwitterUser.objects.all())])
                                    
    password = serializers.CharField(min_length=3)


    def create(self, validated_data):
        user = TwitterUser.objects.create_user(validated_data['username'], 
                                                validated_data['email'],
                                                validated_data['password'])
        return user
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username) 
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        return instance

    class Meta:
        model = TwitterUser
        fields = ('id', 'username', 'email', 'password')


class TwitterUserSerializerForUsers(serializers.ModelSerializer):
    """
    This a general class for the users serializer is meant to be used when viewing all users
    the email is selectivly shown via logic in the UserView class
    """
    class Meta:
        model = TwitterUser
        fields = ('username', 'email')