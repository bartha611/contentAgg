from rest_framework import serializers
from .models import Article, NewsWebsite


class articleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'url']


class websiteSerializer(serializers.ModelSerializer):
    articles = articleSerializer(many=True)

    class Meta:
        model = NewsWebsite
        fields = ['id', 'name', 'category', 'clicks', 'articles']


class websiteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsWebsite
        fields = ['id', 'clicks']
