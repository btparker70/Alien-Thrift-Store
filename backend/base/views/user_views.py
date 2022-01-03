from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from django.contrib.auth.models import User
from base.serializers import ProductSerializer, UserSerializer, UserSerializerWithToken

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth.hashers import make_password
from rest_framework import status

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
  def validate(self, attrs):
    data = super().validate(attrs)

    # data['username'] = self.user.username
    # data['email'] = self.user.email

    serializer = UserSerializerWithToken(self.user).data

    for key, value in serializer.items():
      data[key] = value
    
    return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['POST'])
def registerUser(req):
  data = req.data
  
  try:
    user = User.objects.create(
      first_name = data['name'],
      username = data['email'],
      email = data['email'],
      password = make_password(data['password']),
    )
    serializer = UserSerializerWithToken(user, many=False)

    return Response(serializer.data)
  except:
    message = {'detail': 'User with this email already exists'}
    return Response(message, status=status.HTTP_400_BAD_REQUEST)

# this gives us access to the default user data based on
# the information passed through the access token
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(req):
  user = req.user
  serializer = UserSerializer(user, many=False)
  return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(req):
  users = User.objects.all()
  serializer = UserSerializer(users, many=True)
  return Response(serializer.data)