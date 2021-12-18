from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product

# this serializer wraps around product model
# turn it into json for front end
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
      model = Product
      fields = '__all__'