# 引入表单类
from django import forms
# 引入模型
from django.contrib.auth.models import User
from . import models


# 登录
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


# 写文章
class ArticleForm(forms.Form):
    title = forms.CharField()
    category = forms.CharField()
    # img = forms.CharField()
    # body = forms.CharField()
    # rendering = forms.CharField()
