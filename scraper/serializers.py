from rest_framework import serializers
from .models import Article, NewsWebsite


class articleSerializer(serializers.ModelSerializer):
    news_website = serializers.StringRelatedField()

    class Meta:
        model = Article
        fields = ['news_website', 'title', 'url']
