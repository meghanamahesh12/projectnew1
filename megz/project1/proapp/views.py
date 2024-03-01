from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate
from django.urls import reverse


# Create your views here.
def index(request):
    if (request.method=='POST'):
        username = request.POST.get('uesername')
        password = request.POST.get('password')
        user = authenticate (request,username=username, password=password)
        if user is not None:
            index(request,user)
            return redirect(reverse('home'))
        else:
           pass
        return render(request,'index.html')

def home(request):

    return render(request,'home.html')

def list(request):
    s=Signin.objects.all()
    content={'data':s}
    return render(request,'list.html',content)

def form1(request):
    f1=Listform(request.POST)
    if (request.method=='POST'):
        if f1.is_valid():
            f1.save()
        return list(request)
    return render(request,'listform.html',{'form':f1})
