from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.userHomepage,name = 'userHomepage'),
    path('addpost',views.addpost,name = 'addpost'),
    path('signout',views.signout,name='signout'),
    path('submitpost',views.submitpost,name='submitpost'),
    path('profile',views.profile,name='profile'),
    path('homepage',views.userHomepage,name='userHomepage'),
    path('passwordreset',views.passwordReset,name='passwordReset'),

    
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

