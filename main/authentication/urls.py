from django.urls import path
from .views import user_login,user_logout,signup

urlpatterns = [

    path('',user_login, name='userlogin'),
    path('logout/',user_logout, name='userlogout'),
    path('signup/',signup, name='signup'),
]

