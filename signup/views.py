from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from userHomepage.models import UserPreference


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
        new_preference = UserPreference(user=username, Science=True, Math=True,
                                        History=True, Programming=True, cs=True, cpp=True, ml=True, iot=True,
                                        Robots=True,
                                        Space=True, Literature=True, appD=True, Political=True, Sports=True,
                                        Cricket=True,
                                        Bollywood=True, Hollywood=True, TV=True, Life=True)

        new_preference.save()
        print("created")
        return redirect('signin')
    else:
        return render(request,'signup.html')

def signin(request):
    return redirect('/signin')