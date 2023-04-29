from django import forms
from django.forms import ModelForm

from .models import User, Article

class UserForm (ModelForm):
    class Meta:
        model = User
        fields = "__all__"

class ArticleForm (ModelForm):
    class Meta:
        model = Article
        fields = "__all__"