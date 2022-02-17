from django.urls import URLPattern, path,re_path
from . import views

urlpatterns = [
    path('', views.Index.as_view() , name='index')

]