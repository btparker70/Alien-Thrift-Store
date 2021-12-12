# this file connects the views to urls
from django.urls import path
from . import views

# when you go to these routes, load these views
urlpatterns = [
  # homepage
  path('', views.getRoutes, name="routes"),
  path('products/', views.getProducts, name="products"),
  path('products/<str:pk>', views.getProduct, name="product"),
]