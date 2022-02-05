# this file connects the views to urls
from django.urls import path
from base.views import user_views as views


# when you go to these routes, load these views
urlpatterns = [
  # homepage
  path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

  path('register/', views.registerUser, name='register'),

  path('profile/', views.getUserProfile, name="users-profile"),
  path('profile/update/', views.updateUserProfile, name="user-profile-update"),
  path('', views.getUsers, name="users"),
]