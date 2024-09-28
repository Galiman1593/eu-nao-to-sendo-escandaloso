from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def index(request):
    return HttpResponse('estou na web! ')

def segundo(request):
    return HttpResponse('<h1>segundo</h1>')