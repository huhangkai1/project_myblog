from django.shortcuts import render
from .models import ArticlePost


# Create your views here.

# 博客主页
def article_index(request):
    # 取出所有文章
    articles = ArticlePost.objects.all()
    context = {'articles': articles}
    return render(request, 'article/index.html', context)