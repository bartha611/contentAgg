from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from scraper.models import NewsWebsite, Article
import requests


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        website_id = NewsWebsite.objects.get(name="Chicago Tribune")
        Article.objects.filter(news_website=website_id).delete()
        page = requests.get("https://www.chicagotribune.com/")
        soup = BeautifulSoup(page.text, 'html.parser')
        total = 0
        for link in soup.find_all(class_="recommender"):
            if total < 10:
                article = Article()
                article.news_website = website_id
                article.title = link.get_text().strip()
                article.url = link.find('a')['href']
                article.save()
                total += 1
            else:
                break
