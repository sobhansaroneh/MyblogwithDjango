from ast import Return
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def shop(request):
    return HttpResponse('Hello World!!!!!!!')


def blog(request):
    return HttpResponse('here is blog')