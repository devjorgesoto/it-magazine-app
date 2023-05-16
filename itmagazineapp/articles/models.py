from django.db import models
from users.models import User # importing data from another model.

class Article (models.Model):

    id = models.BigAutoField(primary_key=True) # not in forms
    user = models.ForeignKey (User, on_delete=models.CASCADE)

    headline = models.TextField(max_length=60)
    description = models.TextField (max_length=160)
    body = models.TextField (max_length=4000)
    
    date_published = models.DateField(auto_now=True) # not in forms
    location = models.CharField(max_length=30, null=True, blank=True)

    article_pic = models.ImageField(default='milad-fakurian-unsplash-article.jpg')

    class Meta:
        db_table = 'article_table'
 
    #approve = models.IntegerField(null=True) # not in forms
    #tags = models.CharField(max_length=30,null=True, blank=True) # not in forms # create class?
    #reading_time = models.IntegerField() # not in forms
    
#class Tags (models.Model) #? Remove tags in articles.
#class Approve (models.Model) #? Remove tags in articles.
