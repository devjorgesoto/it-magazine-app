from django.shortcuts import render
from django.http import HttpResponse

from .forms import UserForm, ArticleForm
from .models import User, Article

def workspace (request):
    
    form_article = ArticleForm(request.POST or None)

    if form_article.is_valid():
            form_article.save()   

    context = {'form_article':form_article }
    return render (request, "workspace.html", context )   

def profile (request):
    
    form_user = UserForm(request.POST or None)

    if form_user.is_valid():
      form_user.save()   

    context = {'form_user':form_user }
    return render (request, "profile.html", context )

def home(request):

    article_result = Article.objects.all()

    context = {'article_result' : article_result}

    return render(request, 'home.html', context)
