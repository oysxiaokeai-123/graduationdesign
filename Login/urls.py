from django.urls import path
from . import views

urlpatterns =[
    path('',views.LoginPage),
    path('loginResult',views.loginResult),
    path('reLogin',views.reLogin),
]