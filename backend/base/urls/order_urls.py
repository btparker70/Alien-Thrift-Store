# this file connects the views to urls
from django.urls import path
from base.views import order_views as views


# when you go to these routes, load these views
urlpatterns = [
  path('add/', views.addOrderItems, name='orders-add'),
  path('<str:pk>/', views.getOrderById, name='user-order'),
]