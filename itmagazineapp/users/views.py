from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm
from .user_db_test import prepopulate_db_user
from articles.models import Article 

'''
def home(request):

    user_obj = User.objects.all()

    prepopulate_db_user()

    context = {'user_obj':user_obj}

    return render(request, 'users/user_test.html', context)
'''

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
    return render (request,"users/user.html", context)

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
                return redirect('/users/user/'+ str(user_obj.id))

    # context and return
    context = {'user_obj' : user_obj, 'form_user' : form_user }
    return render (request, "users/edit-user.html", context)

def sign_up(request):
    
    form_user = UserForm(request.POST or None)

    if form_user.is_valid():
      form_user.save()   

    # context and return
    context = {'form_user':form_user }
    return render (request, "users/sign_up.html", context )


