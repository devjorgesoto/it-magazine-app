from django.shortcuts import render
from django.http import HttpResponse

from .forms import WriterForm , ReaderForm, ArticleForm
from .models import Writer, Reader, Article

def register_result (request):
      writer_result = Writer.objects.all()

      context = {
            
        'writer_result' : writer_result

      }

      return render(request, 'register_result.html', context)
      

def home(request):

    # Form Writer

    form_writer = WriterForm(request.POST or None)
    
    if form_writer.is_valid():
        form_writer.save()

    # Form Reader
    form_reader = ReaderForm(request.POST or None)

    if form_reader.is_valid():
            form_reader.save()    

    # Form Article
    form_article = ArticleForm(request.POST or None)

    if form_article.is_valid():
            form_article.save()   

    
    # Context

    context = {
         
         'form_writer':form_writer,
         'form_reader':form_reader,
         'form_article':form_article,
         
    }

    return render (request, "home.html" , context)
