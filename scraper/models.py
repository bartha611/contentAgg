from django.db import models

# Create your models here.


class NewsWebsite(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Article(models.Model):
    news_website = models.ForeignKey(NewsWebsite, on_delete=models.CASCADE)
    url = models.URLField()
    title = models.CharField(max_length=200)

    def __str__(self):
        return "{} {}".format(self.title, self.title)

    def __unicode__(self):
        return self.title
