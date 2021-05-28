from django.urls import path
from django.urls.resolvers import URLPattern
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[
    path('login/',obtain_auth_token),
    path('register/')
]