from django.core.management.base import BaseCommand
from scraper.models import NewsWebsite
from django.conf import settings
import requests


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        response = requests.get(
            "http://newsapi.org/v2/sources?language=en&apiKey={}".format(settings.NEWSAPI))
        for website in response.json()["sources"]:
            newWebsite = NewsWebsite()
            newWebsite.name = website["name"]
            newWebsite.search_id = website["id"]
            newWebsite.category = website["category"]
            newWebsite.url = website["url"]
            newWebsite.save()
            print(newWebsite)
