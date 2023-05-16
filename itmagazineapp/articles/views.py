from django.shortcuts import render, redirect

from .models import Article
from .forms import ArticleForm

from users.models import User

from comments.models import Comment
from comments.forms import CommentForm

from .article_db_test import prepopulate_db_article

import datetime, random

# global variables

now_time = datetime.datetime.now()

# functions

def home(request):

    article_obj = Article.objects.all()

    prepopulate_db_article()

    # context and return
    context = {'article_obj' : article_obj }
    return render(request, 'home.html', context)

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

# this method/view display one article and several comments, included a form for new comments.
def article(request ,article_id):
    
    article_obj= Article.objects.get(id=article_id)

    # show comments
    # only show comments related (filtered) to the article, not from other articles
    comments_all = Comment.objects.all()

    comments_by_article = []

    for comment in comments_all:
        if comment.article.id == article_id:
            comments_by_article.append(comment)

    # create new comments
    random_user = User.objects.get(id=random.randint(1,10))
    comment = Comment( user = random_user, article = article_obj)
   
    form_comment = CommentForm(request.POST, instance=comment)
        
    if form_comment.is_valid():
        form_comment.save()
        return redirect('/articles/article/'+ str(article_id))

    # context and return
    context = {'article_obj' : article_obj, 'comments_by_article':comments_by_article, 'form_comment':form_comment }
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
            return redirect('/articles/article/'+ str(article_obj.id))
        
    # context and return
    context = {'article_obj' : article_obj, 'form_article' : form_article }
    return render (request, "edit-article.html", context)