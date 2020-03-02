from django.core.management.base import BaseCommand
from scraper.models import NewsWebsite, Article
import requests


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        secret = "UXflRrJ3G3RHvHuZ4RAu5j6w4vNy05vg"
        response = requests.get(
            "https://api.nytimes.com/svc/topstories/v2/home.json?api-key={}".format(secret))
        i = 0
        for article in response.json()["results"]:
            if i < 10:
                url = article["url"]
                title = article["title"]

                i += 1
            else:
                pass
