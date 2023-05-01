from django.shortcuts import render
from django.http import HttpResponse

from .forms import UserForm, ArticleForm
from .models import User, Article

def profile(request, user_id):
    
    profile_obj = User.objects.get(id=user_id)

    context = {'profile_obj':profile_obj}
    return render (request,"profile.html", context)
    

def read(request ,article_id):
    
    article_obj= Article.objects.get(id=article_id)
    
    #print (article_obj.description)
    
    context = {'article_obj' : article_obj }
    return render (request, "read.html", context)

def workspace (request):
    
    form_article = ArticleForm(request.POST or None)

    if form_article.is_valid():
            form_article.save()   

    context = {'form_article':form_article }
    return render (request, "workspace.html", context )   

def sign_up(request):
    
    form_user = UserForm(request.POST or None)

    if form_user.is_valid():
      form_user.save()   

    context = {'form_user':form_user }
    return render (request, "sign_up.html", context )

def home(request):

    article_obj = Article.objects.all()

    context = {'article_obj' : article_obj}

    return render(request, 'home.html', context)
