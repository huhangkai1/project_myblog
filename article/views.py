from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
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


# 写文章
@login_required(login_url="article/index")
def article_create(request):
    # 判断用户是否提交数据
    if request.method == "POST":
        if 'rendering' in request.POST:
            data = request.POST
            # 获取所有类别
            classifications = models.Classification.objects.all()
            # 创建表单类实例
            article = models.ArticlePost()
            article.title = data.title
            article.category = data.category
            article.img = data.img
            article.body = data.body

            context = {'classifications': classifications, 'article': article}
            # 将提交的数据赋值到表单实例中

        return render(request, 'article/create.html', context)


        if 'rendering' in request.POSTs:
            print(context)

            return render(request, 'article/create.html', context)
        elif request.POST.has_key('update'):
            # 判断提交的数据是否满足模型的要求
            if articlePost.is_valid():
                # 保存数据，但暂时不提交到数据库中
                new_article = articlePost.save(commit=False)
                # 指定登录的用户为作者
                new_article.author = User.objects.get(id=request.user.id)
                # 将新文章保存到数据库中
                new_article.save()
                # 完成后返回到文章列表
                return redirect("article:article_list")
                # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 如果用户请求获取数据
    else:
        # 获取所有类别
        classifications = models.Classification.objects.all()
        # 创建表单类实例
        article = models.ArticlePost()
        # 赋值上下文
        context = {'classifications': classifications, 'article': article}
        # 返回模板
        return render(request, 'article/create.html', context)


# 将markdown语法渲染成html样式
def article_rendering(request):
    context = models.ArticlePost(data=request.POST)
    print(context)
    return render(request, 'article/create.html', context)


# 用户登录
def article_login(request):
    if request.method == 'POST':
        loginForm = form.LoginForm(data=request.POST)
        if loginForm.is_valid():
            # 清洗出合法数据
            data = loginForm.cleaned_data
            print(data)
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return redirect("article:article_index")
            else:
                print("账号或密码输入有误。请重新输入~")
                return HttpResponse("账号或密码输入有误。请重新输入~")
        else:
            print("输入有误。请重新输入~")
            return redirect("article:article_index")


# 用户登录
def article_logout(request):
    logout(request)
    return redirect("article:article_index")



