from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    selecctData = myProfile.objects.all()
    sellectedData = Gallery.objects.all()
    context ={
     'data1':selecctData,
     'data2':sellectedData,
    }
    return render(request,'index.html',context)
