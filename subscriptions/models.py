from django.db import models
from scraper.models import NewsWebsite
from Profile.models import Profile

# Create your models here.


class Subscription(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    news_website = models.ForeignKey(NewsWebsite, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.profile) + " " + str(self.news_website)
