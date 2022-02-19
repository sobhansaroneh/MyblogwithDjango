from unicodedata import name
from django.urls import URLPattern, path,re_path
from . import views

urlpatterns = [
    path('index', views.Index.as_view() , name='index'),
    path('', views.Index.as_view() , name='index'),
    path('about' , views.about.as_view() , name = 'about'),
    path('post' , views.post.as_view() , name='post'),
    path('contact' , views.contact.as_view(),name='contact')


]