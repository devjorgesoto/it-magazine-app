from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse


from .forms import UserForm, ArticleForm
from .models import User, Article

def profile(request, user_id):
    
    profile_obj = User.objects.get(id=user_id)

    context = {'profile_obj':profile_obj}
    return render (request,"profile.html", context)
    

def read(request ,article_id):
    
    article_obj= Article.objects.get(id=article_id)
    
    context = {'article_obj' : article_obj }
    return render (request, "read.html", context)

def edit_article(request ,article_id):
    
    article_obj= Article.objects.get(id=article_id)

    # show existing article in edit(form) mode. just show !!!
    # for new forms => form_article = ArticleForm(request.POST or None)
    form_article = ArticleForm(instance=article_obj) 
    
    # update edited article
    # this if keeps form pre-populated, without this line = blank form
    if request.method == 'POST': 
        form_article = ArticleForm(request.POST, instance=article_obj)

        if form_article.is_valid():
                form_article.save()
                return redirect('/read/'+ str(article_obj.id)) # Correct?

    context = {'article_obj' : article_obj, 'form_article' : form_article }
    return render (request, "edit_article.html", context)

def workspace (request):

    # preview existing articles
    article_obj= Article.objects.all()

    # create new article
    form_article = ArticleForm(request.POST or None)

    if form_article.is_valid():
            form_article.save()  

    # context and return
    context = {'form_article':form_article, 'article_obj':article_obj}
    return render (request, "workspace.html", context )   

def sign_up(request):
    
    form_user = UserForm(request.POST or None)

    if form_user.is_valid():
      form_user.save()   

    context = {'form_user':form_user }
    return render (request, "sign_up.html", context )

def home(request):

    article_obj = Article.objects.all()

    context = {'article_obj' : article_obj }

    return render(request, 'home.html', context)
