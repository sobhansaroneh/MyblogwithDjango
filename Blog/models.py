from django.contrib.auth.models import User
from django.db import models
from django.forms import CharField
from ckeditor.fields import RichTextField


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    First_name = models.CharField(max_length=20, verbose_name='نام')
    Last_name = models.CharField(max_length=40, verbose_name='نام خانوادگی')
    description = RichTextField(max_length=250)
    join_date = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.First_name} {self.Last_name}"

    class Meta:
        verbose_name = 'نویسنده'
        verbose_name_plural = "نویسنده‌ها"


class Article(models.Model):
    title = models.CharField(max_length=30)
    content = RichTextField(max_length=1000)
    created = models.DateField(auto_now=True)
    writer = models.ForeignKey('Author', on_delete=models.CASCADE),
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = "مقالات"
