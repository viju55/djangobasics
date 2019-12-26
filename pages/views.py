from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'index.html',{})


def index(request):
    return render(request, 'design.html',{})

def display(request, id):
    return render(request, 'display.html',{})

def data(request):
    return render(request, 'data.html',{})