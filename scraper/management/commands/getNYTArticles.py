from django.core.management.base import BaseCommand
from scraper.models import NewsWebsite, Article
from django.conf import settings
import requests


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        secret = settings.NYTIMESAPI
        website = NewsWebsite.objects.get(name="NY Times")
        Article.objects.filter(news_website=website).delete()
        response = requests.get(
            "https://api.nytimes.com/svc/topstories/v2/home.json?api-key={}".format(secret))
        i = 0
        for article in response.json()["results"]:
            if i < 10:
                url = article["url"]
                title = article["title"]
                entry = Article(title=title, url=url, news_website=website)
                entry.save()
                print("added article with title {}".format(title))
                i += 1
            else:
                break
