from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.userHomepage,name = 'userHomepage'),
    path('addpost',views.addpost,name = 'addpost'),
    path('signout',views.signout,name='signout'),
    path('submitpost',views.submitpost,name='submitpost'),
    path('profile',views.profile,name='profile'),
    path('homepage',views.userHomepage,name='userHomepage'),
    
]
