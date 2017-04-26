from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Admin Portal Under Costruction</h1>')