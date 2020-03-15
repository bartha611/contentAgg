from django.db import models
import datetime


# Create your models here.

categories = (
    ("BUSINESS", "business"),
    ("GENERAL", "general"),
    ("SPORTS", "sports"),
    ("ENTERTAINMENT", "entertainment"),
    ("TECHNOLOGY", "technology"),
    ("SCIENCE", "science")
)


class NewsWebsite(models.Model):
    name = models.CharField(max_length=200)
    search_id = models.CharField(max_length=200)
    url = models.URLField()
    category = models.CharField(
        choices=categories, default="general", max_length=15)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Article(models.Model):
    news_website = models.ForeignKey(
        NewsWebsite, related_name="articles", on_delete=models.CASCADE)
    url = models.URLField()
    title = models.CharField(max_length=200)
    createdat = models.DateField(
        auto_now_add=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
