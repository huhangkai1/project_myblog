from django.urls import path, include
from django.conf import settings
from django.views.static import serve

from . import views

app_name = 'article'

urlpatterns = [
    #path('index', views.article_index, name='article_index'),


]
