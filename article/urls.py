from django.urls import path, include


from . import views

app_name = 'article'

urlpatterns = [
    # 博客主页
    path('index', views.article_index, name='article_index'),
    # 写文章
    path('create', views.article_create, name='article_create'),


    # 登录
    path('login', views.article_login, name='article_login'),
    # 退出登录
    path('logout', views.article_logout, name='article_logout'),

    # # 文章详情
    # path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
    # # 写文章
    # path('article-create/', views.article_create, name='article_create'),
    # # 删除文章
    # path('article-delete/<int:id>/', views.article_delete, name='article_delete'),
    # # 更新文章
    # path('article-update/<int:id>/', views.article_update, name='article_update'),

]
