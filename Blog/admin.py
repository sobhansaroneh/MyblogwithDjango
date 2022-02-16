from atexit import register
from faulthandler import is_enabled
from pyexpat import model
from xml.dom.expatbuilder import Rejecter
from django.contrib import admin

from Blog.models import Article, Author


class DetailAuthor(admin.ModelAdmin):
    list_display = ['Last_name' , 'join_date','is_active']
    list_filter = ('join_date','is_active')
    search_fields = ('First_name' , 'Last_name')
    list_editable = ['is_active']
    actions = ['act']

    def act(self , request , queryset):
        pass

admin.site.register(Author , DetailAuthor)

admin.site.register(Article)