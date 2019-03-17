from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import models
from . import form


# 博客主页
def article_index(request):
    # 取出所有文章
    articles = models.ArticlePost.objects.all()
    # 需要传递给模板（templates）的对象
    context = {'articles': articles}
    # render函数：载入模板，并返回context对象
    return render(request, 'article/index.html', context)


# 用户登录
def article_login(request):
    print("#########ok", request.method)
    if request.method == 'POST':
        print("#########ok")
        # loginForm = form.LoginForm(data=request.POST)
        # print(loginForm)
        # if loginForm.is_valid():
        #     # 清洗出合法数据
        #     data = loginForm.cleaned_data
        #     user = authenticate(username=data['username'], password=data['password'])
        #     if user:
        #         login(request, user)
        #         return redirect("article:article_index")
        #     else:
        #         print("账号或密码输入有误。请重新输入~")
        #         # return HttpResponse("账号或密码输入有误。请重新输入~")
        # else:
        #     print("输入有误。请重新输入~")
        #     # return HttpResponse("账号或密码输入有误。输入~")
    elif request.method == 'GET':
        loginForm = form.LoginForm()
    return redirect("article:article_index")




