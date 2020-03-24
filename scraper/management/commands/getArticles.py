from django.core.management.base import BaseCommand
from scraper.models import Article, NewsWebsite
from django.conf import settings
import requests


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        response = requests.get(
            "http://newsapi.org/v2/sources?language=en&apiKey={}".format(settings.NEWSAPI))
        for source in response.json()["sources"]:
            website = NewsWebsite.objects.get(name=source["name"])
            Article.objects.filter(news_website=website).delete()
            articles = requests.get(
                "http://newsapi.org/v2/top-headlines?sources={}&apiKey={}".format(source["id"], settings.NEWSAPI))
            if articles.status_code == 200:
                for article in articles.json()["articles"]:
                    entry = Article()
                    entry.news_website = website
                    entry.url = article["url"]
                    entry.title = article["title"]
                    entry.save()
            else:
                continue
