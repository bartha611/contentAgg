from django.core.management.base import BaseCommand
from redditScraper.models import Article, NewsWebsite
import praw


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        client_id = "GjizdjzSS5Rm9Q"
        client_secret = "x75mtpDyQkNRqeSr7d3powXMzKg"
        user_agent = "/u/lethargicriver making a News Content Aggregate website"
        reddit = praw.Reddit(
            client_id=client_id, client_secret=client_secret, user_agent=user_agent)
        for submission in reddit.subreddit("worldnews").hot(limit=10):
            url = "https://reddit.com/r/worldnews/{}".format(submission)
            title = submission.title
            site = NewsWebsite.objects.get(name="Reddit")
            article = Article(url=url, title=title, news_website=site)
            article.save()
