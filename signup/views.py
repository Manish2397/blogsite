from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth


# Create your views here.

def signup(request):
    if(request.method == 'POST'):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        new_user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
        new_user.save()
        print("created")
        return redirect('/')
    else:
        return render(request,'signup.html')

def signin(request):
    return redirect('/signin')