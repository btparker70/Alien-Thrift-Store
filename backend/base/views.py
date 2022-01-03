from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from django.contrib.auth.models import User
from .models import Product
from .products import products
from .serializers import ProductSerializer, UserSerializer, UserSerializerWithToken

# Create your views here.
# views are key components of the application within django
# they take web requests and return web response
# api_view is a decorator that makes the response pretty

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

@api_view(['GET'])
def getProducts(req):
  # return all products from db
  products = Product.objects.all()
  serializer = ProductSerializer(products, many=True)
  return Response(serializer.data)

# pk = primary key
# search all products by id return that id
@api_view(['GET'])
def getProduct(req, pk):
  product = Product.objects.get(_id=pk)
  serializer = ProductSerializer(product, many=False)
  return Response(serializer.data)