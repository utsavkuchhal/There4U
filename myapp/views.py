import re
from django.http import Http404
from django.http.response import HttpResponse
from myapp.models import User
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, status
from .serializers import UserSerializer
from .models import User
# from rest_framework.authtoken.models import Token

class UserList(APIView):

    def post(self, request):
        serializer = UserSerializer(data= request.data)
        if serializer.is_valid():
            # temp = serializer.save().id
            # token = Token.objects.get_or_create(user = temp)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        return Response(status = status.HTTP_400_BAD_REQUEST)

class UpdateUser(APIView):
    pass


def home(request):
    return HttpResponse("This is a home page")