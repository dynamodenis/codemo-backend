from django.contrib.auth import authenticate
from rest_framework import serializers
# from .models import User

from django.contrib.auth import get_user_model
User=get_user_model()


class MentorRegistrationSerializer(serializers.ModelSerializer):

    '''Serializers registration requests and creates a new mentor users.'''

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password', 'is_mentor']

    def create(self, validated_data):
        return User.objects.create_mentor(**validated_data)


class StudentRegistrationSerializer(serializers.ModelSerializer):

    '''Serializers registration requests and creates new student users.'''

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )


    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password', 'is_student']

    def create(self, validated_data):
        return User.objects.create_student(**validated_data)


class UserSerializer(serializers.ModelSerializer):

    '''Handles serialization and deserialization of User objects.'''

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password')

        # read_only_fields = ('token',)

