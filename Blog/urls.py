from django.urls import URLPattern, path,re_path
from . import views

urlpatterns = [
    path('blog/', views.blog)

]