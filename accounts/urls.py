from django.urls import path
from .views import *


app_name= 'accounts'


urlpatterns = [
    path('',Login,name="Login"),
    path('logout/',logout,name="logout"),
    path('home/',home,name="home"),
]
