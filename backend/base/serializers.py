from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product

# serializers convert complex datasets into native python
class UserSerializer(serializers.ModelSerializer):
    class Meta:
      model = User
      fields = ['id', 'username', 'email']

# this serializer wraps around product model
# turn it into json for front end
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
      model = Product
      fields = '__all__'