from django import forms
from django.forms import ModelForm

from .models import Writer, Reader, Article

class WriterForm (ModelForm):
    class Meta:
        model = Writer
        fields = "__all__"

class ReaderForm (ModelForm):
    class Meta:
        model = Reader
        fields = "__all__"

class ArticleForm (ModelForm):
    class Meta:
        model = Article
        fields = "__all__"