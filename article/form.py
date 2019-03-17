# 引入表单类
from django import forms
# 引入模型


class LoginForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField()
