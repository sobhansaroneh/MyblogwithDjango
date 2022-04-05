from ast import Return
from re import template
from urllib import request
from venv import create
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import *


class Index(TemplateView):
    
    def get(self , request , **kwargs):
        
        article_data = []
        # all_article = Article.objects.all().order_by('-created')[:4]
        # for article in all_article:
        #     article_data.append({
        #         'title':article.title,
        #         'description': article.content,
        #         'date' : article.created,
        #     })
        #
        context = {
            'article_data': Article.objects.all().order_by('-created')[:4]
        }
        return render(request , 'index.html' , context)

class post(TemplateView):
    def get(self, request ,**kwargs):
        article_data = []
        all_article = Article.objects.all().order_by('-created')[:3]
        for article in all_article:
            article_data.append({
                'title':article.title,
                'description': article.content,
                'date' : article.created,
            })
        
        context = {
            'article_data' :article_data
        }
        return render(request, 'post.html', context)


class about(TemplateView):
    def get(self, request ,**kwargs):
        return render(request,'about.html')


class contact(TemplateView):
    def get(self , request ,**kwargs):
        return render(request,'contact.html')


class DetailPost(TemplateView):
    def get(self,request, id):
        article = Article.objects.get(id=id)
        context = {
            'article': article
        }
        return render(request, 'detail_post.html', context=context)
