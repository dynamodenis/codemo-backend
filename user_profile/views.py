from django.shortcuts import render
from .serializers import ProfileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from django.contrib.auth import get_user_model
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.http import request



# Create your views here.

class ProfileAPI(APIView):
    # permission_classes=(AllowAny,)
    permission_classes=(IsAuthenticated,)
    def get_profile(self,pk):
        try:
            User = get_user_model()
            users=User.objects.get(id=pk)

            return Profile.objects.get(pk=users.profile.id)
            
        except Profile.DoesNotExist:
            raise Http404
    
    def get(self,request, format=None):
        profile=self.get_profile(request.user.id)
        serialize=ProfileSerializer(profile)
        return Response(serialize.data)
    
    def put(self,request,pk, format=None):
        profile=self.get_profile(pk)
        serializer=ProfileSerializer(profile,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    
