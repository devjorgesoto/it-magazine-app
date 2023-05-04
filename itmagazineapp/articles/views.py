from django.shortcuts import render, redirect
from .forms import UserForm, ArticleForm, CommentForm
from .models import User, Article, Comment
import datetime

# global variables

now_time = datetime.datetime.now()

# functions

def home(request):

    article_obj = Article.objects.all()

    # context and return
    context = {'article_obj' : article_obj }
    return render(request, 'home.html', context)

def sign_up(request):
    
    form_user = UserForm(request.POST or None)

    if form_user.is_valid():
      form_user.save()   

    # context and return
    context = {'form_user':form_user }
    return render (request, "sign_up.html", context )

def workspace (request):

    # preview existing articles
    article_obj= Article.objects.all()

    # create new article
    form_article = ArticleForm(request.POST or None)

    if form_article.is_valid():
            form_article.save()  

    # context and return
    context = {'article_obj':article_obj, 'form_article':form_article,}
    return render (request, "workspace.html", context )   

def user(request, user_id):
    
    user_obj = User.objects.get(id=user_id)

    # all articles without filter
    # in html call this as 'article_obj'
    article_obj = Article.objects.all()

    # all articles filtered by user
    # in html call this filter as 'article_obj_by_user'
    article_obj_by_user = []

    for article in article_obj:

        if article.user.id == user_id:

            article_obj_by_user.append(article)

    # context and return
    context = {'user_obj':user_obj, 'article_obj':article_obj, 'article_obj_by_user':article_obj_by_user}
    return render (request,"user.html", context)

def edit_user(request ,user_id):
    
    user_obj= User.objects.get(id=user_id)

    # show existing article in edit(form) mode. just show !!!
    # for new forms => form_article = ArticleForm(request.POST or None)
    form_user = UserForm(instance=user_obj) 
    
    # update edited article
    # this if keeps form pre-populated, without this line = blank form
    if request.method == 'POST': 
        form_user = UserForm(request.POST, instance=user_obj)

        if form_user.is_valid():
                form_user.save()
                return redirect('/user/'+ str(user_obj.id))

    # context and return
    context = {'user_obj' : user_obj, 'form_user' : form_user }
    return render (request, "edit-user.html", context)

def article(request ,article_id):
    
    article_obj= Article.objects.get(id=article_id)

    # show comments
    # only show comments related (filtered) to the article, not from other articles
    comments_all = Comment.objects.all()

    comments_obj_by_article = []

    for comment in comments_all:
        if comment.article.id == article_id:
            comments_obj_by_article.append(comment)

    # create new comments
    comment = Comment( user = article_obj.user, article = article_obj)
   
    form_comment = CommentForm(request.POST, instance=comment)
        
    if form_comment.is_valid():
        form_comment.save()
        return redirect('/article/'+ str(article_id))

    # context and return
    context = {'article_obj' : article_obj, 'comments_obj_by_article':comments_obj_by_article, 'form_comment':form_comment }
    return render (request, "article.html", context)

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
            return redirect('/article/'+ str(article_obj.id)) # Correct?
        
    # context and return
    context = {'article_obj' : article_obj, 'form_article' : form_article }
    return render (request, "edit-article.html", context)

# utils functions
    
