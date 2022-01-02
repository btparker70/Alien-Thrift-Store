from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product

# serializers convert complex datasets into native python
# this gets the user data from the django user model
class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
      model = User
      fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin']

    def get__id(self, obj):
      return obj.id
    
    def get_isAdmin(self, obj):
      return obj.is_staff
    
    def get_name(self, obj):
      name = obj.first_name
      if name == '':
        name = obj.email

      return name

# this serializer wraps around product model
# turn it into json for front end
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
      model = Product
      fields = '__all__'