from ast import Return
from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'index.html'
    
