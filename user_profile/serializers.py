from rest_framework import serializers
from .models import Profile,Test
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import serializers, status
# from ...hackerRank.apps.authentication.models import User


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email','is_student','is_mentor']


class ProfileSerializer(serializers.ModelSerializer):
    """
    A student serializer to return the student details
    """
    user = UserSerializer(read_only=True)
    
    # picture = Base64ImageField(
    #     max_length=None, use_url=True,
    # )
    class Meta:
        model=Profile
        fields=('user','id','picture','location','bio','education','company')


    from rest_framework import serializers    

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of student
        :return: returns a successfully created student record
        """
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        student, created = Project.objects.update_or_create(user=user,
                            subject_major=validated_data.pop('subject_major'))
        return student
