from rest_framework import serializers
from .models import ShopUser
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('username',)

    def create(self,validated_data):
        lerele = User.objects.create_user(
            username = validated_data.get('username')
        )
        return lerele



class RegisterSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ShopUser
        fields = ('username', 'password', 'email', 'mobile')

    def create(self,validated_data):
        user = ShopUser.objects.create(
            username = validated_data.get('username'),
            password = make_password(validated_data.get('password')),
            email = validated_data.get('email'),
            mobile = validated_data.get('mobile')
        )

        return user