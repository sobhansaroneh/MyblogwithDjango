from pyexpat import model
from django.contrib import admin

from Blog.models import Article, Author



admin.site.register(Author)
admin.site.register(Article)