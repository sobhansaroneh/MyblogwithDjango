from time import timezone
from django.db import models
from django.forms import CharField
from ckeditor.fields import RichTextField
class Author (models.Model):
    First_name = models.CharField(max_length=20)
    Last_name = models.CharField(max_length=40)
    description =  RichTextField(max_length=250)
    join_date = models.DateField(auto_now=True)


class Article(models.Model):
    title = models.CharField(max_length=30)
    content  = RichTextField(max_length=1000)
    created = models.DateField(auto_now=True)
