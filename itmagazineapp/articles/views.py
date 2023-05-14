from django.shortcuts import render, redirect
from .forms import ArticleForm, CommentForm
from .models import Article, Comment
from .article_db_test import prepopulate_db_article
import datetime

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


    
