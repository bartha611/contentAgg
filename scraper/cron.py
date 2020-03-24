from scraper.models import NewsWebsite, Article
from django.conf import settings
from bs4 import BeautifulSoup
import requests


def getNytArticles():
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
            i += 1
        else:
            break


def getArticles():
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


def getTribuneArticles():
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
