# 引入表单类
from django import forms
# 引入模型
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()



