from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .products import products

# Create your views here.
# views are key components of the application within django
# they take web requests and return web response
# api_view is a decorator that makes the response pretty

@api_view(['GET'])
def getRoutes(req):
  routes = [
    '/api/products/',
    '/api/products/create/',

    '/api/products/upload',

    '/api/products/<id>/reciews/',

    '/api/products/top/',
    '/api/products/<id>/',

    '/api/products/delete/<id>/',
    '/api/products/<update>/<id>/',
  ]
  return Response(routes)

@api_view(['GET'])
def getProducts(req):
  return Response(products)

# pk = primary key
# search all products by id return that id
@api_view(['GET'])
def getProduct(req, pk):
  product = None
  for i in products:
    if i['_id'] == pk:
      product = i
      break

  return Response(product)