from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
# Create your views here.
def userHomepage(request):
    return render(request,'userHomepage.html')

def addpost(request):
    return render(request,'addpost.html')

def signout(request):
    auth.logout(request)
    return redirect('signin')