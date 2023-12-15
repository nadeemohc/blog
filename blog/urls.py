from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.signup, name='signup'),
    path('adminlogin/', views.adminlogin, name='blog-adminlogin'),
    path('home/', views.index, name='blog-home'),
    path('adminp/', views.admin, name='blog-admin'),
    path('login/', views.login, name='login'),
    path('home/', views.index, name='blog-index'),
]
