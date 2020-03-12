from django.shortcuts import render
from django.http import Http404
from rest_framework import generics
from .serializers import articleSerializer
from .models import Article, NewsWebsite
# Create your views here.


class articleList(generics.ListAPIView):
    serializer_class = articleSerializer

    def get_queryset(self):
        queryset = Article.objects.all()
        website = self.request.query_params.get('website', None)
        if website is not None:
            try:
                website.replace(" ", "-")
                newsWebsite = NewsWebsite.objects.get(
                    search_id__iexact=website)
                queryset = Article.objects.filter(news_website=newsWebsite.id)
            except:
                raise Http404
        return queryset
