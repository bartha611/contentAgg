from django.urls import path
from . import views

urlpatterns = [
    path('api/articles', views.articleList.as_view())
]
