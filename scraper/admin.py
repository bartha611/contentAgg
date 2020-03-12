from django.contrib import admin
from .models import Article, NewsWebsite

# Register your models here.
admin.site.register(Article)
admin.site.register(NewsWebsite)
