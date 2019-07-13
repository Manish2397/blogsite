from django.shortcuts import render,redirect

# Create your views here.

def signin(request):
    return render(request,'signin.html')

def signup(request):
    return redirect('/signup')