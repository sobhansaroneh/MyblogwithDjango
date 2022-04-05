from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class ArticleViewset(viewsets.ViewSet):
    def list(self, request):
        queryset = Article.objects.all()
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)