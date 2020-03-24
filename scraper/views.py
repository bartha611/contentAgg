from django.shortcuts import render
from django.http import Http404
from rest_framework import generics
from .serializers import websiteSerializer, websiteUpdateSerializer
from .models import Article, NewsWebsite
from rest_framework.permissions import AllowAny
# Create your views here.


class articleList(generics.ListAPIView):
    serializer_class = websiteSerializer

    def get_queryset(self):
        queryset = NewsWebsite.objects.all().order_by('-clicks')
        category = self.request.query_params.get('category', None)
        if category is not None:
            try:
                queryset = NewsWebsite.objects.filter(
                    category__iexact=category).order_by('-clicks')
            except:
                raise Http404
        return queryset


class articleUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = websiteUpdateSerializer
    queryset = NewsWebsite.objects.all()
    permission_classes = [AllowAny, ]
