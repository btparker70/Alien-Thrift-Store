# this file connects the views to urls
from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

# when you go to these routes, load these views
urlpatterns = [
  # homepage
  path('users/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('', views.getRoutes, name="routes"),
  path('products/', views.getProducts, name="products"),
  path('products/<str:pk>', views.getProduct, name="product"),
]