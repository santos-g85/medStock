from django.urls import path
from .views import user_login

urlpatterns = [

    path('login/',user_login, name='userlogin'),
    path('',user_login, name='userlogin'),
]
