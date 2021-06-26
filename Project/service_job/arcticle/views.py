from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Articles
from .serializers import ArticlesSerializer
from rest_framework.generics import get_object_or_404

class ArticlesView(APIView):
    def get(self, request):
        articles = Articles.objects.all()
        serializer = ArticlesSerializer(articles, many=True)
        return Response({"articles": serializer.data})

    def post(self, request):
        articles = request.data.get('articles')
        # Create an article from the above data
        serializer = ArticlesSerializer(data=articles)
        if serializer.is_valid(raise_exception=True):
            articles_saved = serializer.save()
        return Response({"success": "Articles '{}' created successfully".format(articles_saved.title)})

    def put(self, request, pk):
        saved_articles = get_object_or_404(Articles.objects.all(), pk=pk)
        data = request.data.get('articles')
        serializer = ArticlesSerializer(instance=saved_articles, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            articles_saved = serializer.save()
        return Response({
            "success": "Articles '{}' updated successfully".format(articles_saved.title)
        })


    def delete(self, request, pk):
      # Get object with this pk
      articles = get_object_or_404(Articles.objects.all(), pk=pk)
      articles.delete()
      return Response({
        "message": "Articles with id `{}` has been deleted.".format(pk)
      }, status=204)

