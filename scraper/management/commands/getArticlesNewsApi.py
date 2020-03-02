from django.core.management.base import BaseCommand
from scraper.models import Article, NewsWebsite
import requests


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        sources = ["bbc-news", "the-wall-street-journal",
                   "time", "google-news", "cnn", "the-washington-post", "reuters"]
        key = "b7d783cbd1e34982b0903b3a6cdeee1f"
        for source in sources:
            response = requests.get(
                "http://newsapi.org/v2/top-headlines?sources={}&apiKey={}".format(source, key))
            site = NewsWebsite.objects.get(name=source)
            for content in response.json()["articles"]:
                article = Article()
                article.news_website = site.id
                article.title = content["title"]
                article.url = content["url"]
                article.save()
