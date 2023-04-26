from django.shortcuts import render
from django.http import HttpResponse

def home(request):

    context = {}
    return render (request, "home.html" , context)


def article(request):
    context = {}
    return render (request, "article.html" , context )
