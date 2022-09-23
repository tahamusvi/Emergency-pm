from django.urls import path
from .views import *


app_name= 'epm'


urlpatterns = [
    path('home/',home,name="home"),

]
