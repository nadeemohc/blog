from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('nadeem/', views.nadeem, name='blog-nadeem'),
    path('about/', views.about, name='blog-about'),
    path('adminp/', views.admin, name='blog- admin'),
    path('login/', views.login, name='login'),
]
