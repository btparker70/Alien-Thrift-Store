# this file connects the views to urls
from django.urls import path
from base.views import product_views as views


# when you go to these routes, load these views
urlpatterns = [
  path('', views.getProducts, name="products"),
  path('<str:pk>', views.getProduct, name="product"),
]