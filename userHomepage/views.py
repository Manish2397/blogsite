from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import blog


def giveBool(value):
    if(value=='on'):
        return True
    if(value==None):
        return False
# Create your views here.
def userHomepage(request):
    blogs = blog.objects.all().filter(public=1)


    return render(request,'userHomepage.html',{'blogs':blogs})

def addpost(request):
    return render(request,'addpost.html')

def signout(request):
    auth.logout(request)
    return redirect('signin')

def submitpost(request):
    muser = request.user.username
    mtitle = request.POST.get('title')
    mblog = request.POST.get('blog')
    mscience = giveBool(request.POST.get('science'))
    mmaths = giveBool(request.POST.get('maths'))
    mhistory = giveBool(request.POST.get('history'))
    mprogramming = giveBool(request.POST.get('programming'))
    mcs = giveBool(request.POST.get('cs'))
    mcpp = giveBool(request.POST.get('cpp'))
    mml = giveBool(request.POST.get('ml'))
    miot = giveBool(request.POST.get('iot'))
    mrobots = giveBool(request.POST.get('space'))
    mspace = giveBool(request.POST.get('space'))
    mlit =giveBool( request.POST.get('lit'))
    mappD = giveBool(request.POST.get('app'))
    mpol = giveBool(request.POST.get('pol'))
    msports = giveBool(request.POST.get('sports'))
    mcric =giveBool( request.POST.get('cric'))
    mbollywood = giveBool(request.POST.get('bollywood'))
    mhollywood = giveBool(request.POST.get('hollywood'))
    mtv = giveBool(request.POST.get('tv'))
    mlife = giveBool(request.POST.get('life'))
    visibility = request.POST.get('visibility')
    if(visibility=='public'):
        v1=True
        v2=False
    else:
        v1=False
        v2=True

    new_blog = blog(user=muser,blog=mblog,title=mtitle,Science=mscience,Math=mmaths,
    History=mhistory,Programming=mprogramming,cs=mcs,cpp=mcpp,ml=mml,iot=miot,Robots=mrobots,
    Space=mspace,Literature=mlit,appD=mappD,Political=mpol,Sports=msports,Cricket=mcric,
    Bollywood=mbollywood,Hollywood=mhollywood,TV=mtv,Life=mlife,public=v1,private=v2)

    new_blog.save()
    
    
    

    
    
    return render(request,'addpost.html')


def profile(request):
    blogs = blog.objects.all().filter(user=request.user.username)
    return render(request,'profile.html',{'blogs':blogs})
def passwordReset(request):
    return render(request,'passwordResetForm.html')