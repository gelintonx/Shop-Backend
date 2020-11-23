from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import ShopUser
from .serializers import RegisterSerializer, UserSerializer
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# Create your views here.

@api_view(['POST'])
def register(request):
    
    if request.method == 'POST':
        
        register_serializer = RegisterSerializer(data = request.data)
        user_serializer = UserSerializer(data = {"username": request.data['username']} )
        if register_serializer.is_valid():
            register_serializer.save()
        if user_serializer.is_valid():
            user_serializer.save()

            return Response({"Success": "Saved!!"}, status=status.HTTP_201_CREATED)
        else:
            return Response(data=user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):

    if request.method == 'POST':
        
        username = request.data['username']
        password = request.data['password']

        users = ShopUser.objects.get(username=username)

        if users:
            match_password = check_password(password, users.password)

            if match_password == True:
                
                lerele = User.objects.get(username=username)
                print(lerele)
                token = Token.objects.create(user=lerele)
                print(token.key)
                return Response({"Authenticated": True})
            else:
                return Response({"Authenticated": False})
