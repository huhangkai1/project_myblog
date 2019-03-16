from django.shortcuts import render
from .models import ArticlePost


# 博客主页
def article_index(request):
    # 取出所有文章
    articles = ArticlePost.objects.all()
    # 需要传递给模板（templates）的对象
    context = {'articles': articles}
    # render函数：载入模板，并返回context对象
    return render(request, 'article/index.html', context)