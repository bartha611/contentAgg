from django.shortcuts import render
from django.http import Http404
from rest_framework import generics
from .serializers import websiteSerializer
from .models import Article, NewsWebsite
# Create your views here.


class articleList(generics.ListAPIView):
    serializer_class = websiteSerializer

    def get_queryset(self):
        queryset = NewsWebsite.objects.all()
        category = self.request.query_params.get('category', None)
        if category is not None:
            try:
                queryset = NewsWebsite.objects.filter(
                    category__iexact=category)
            except:
                raise Http404
        return queryset
