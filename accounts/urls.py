from django.urls import path
from . import views as viewsA


app_name= 'accounts'


urlpatterns = [
    path('login/',viewsA.Login,name="Login"),
    path('logout/',viewsA.logout,name="logout"),
    path('SignUp/',viewsA.SignUp,name="SignUp"),
]
