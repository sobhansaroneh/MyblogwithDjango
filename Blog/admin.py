from pyexpat import model
from django.contrib import admin

from Blog.models import Article, Author

class DetailAuthor(admin.ModelAdmin):
    list_display = ['Last_name' , 'join_date']
    list_filter = ('join_date',)


admin.site.register(Author , DetailAuthor)
admin.site.register(Article)