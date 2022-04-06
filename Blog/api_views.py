from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


# ViewSet Method
class ArticleViewset(viewsets.ViewSet):
    def list(self, request):
        queryset = Article.objects.all()
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'ok'})
        else:
            return Response(serializer.errors)

    def retrieve(self, pk=None):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass


# Model Views
#
# class ArticleModelSet(viewsets.ModelViewSet):
#     queryset = Article.objects.all()
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
