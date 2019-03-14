from django.urls import path, include


from . import views

app_name = 'article'

urlpatterns = [
    path('index', views.article_index, name='article_index'),


]
