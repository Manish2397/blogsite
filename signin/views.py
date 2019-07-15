from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
# Create your views here.

def signin(request):
    if(request.method=='POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/user')
        else:
            return redirect('signup')
    else:
        return render(request,'signin.html')

def signup(request):
    return redirect('/signup')