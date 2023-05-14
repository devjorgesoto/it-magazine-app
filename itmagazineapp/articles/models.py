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

    class Meta:
        db_table = 'article_table'
 

    #approve = models.IntegerField(null=True) # not in forms
    #tags = models.CharField(max_length=30,null=True, blank=True) # not in forms # create class?
    #reading_time = models.IntegerField() # not in forms
    
    #cover_image = models.ImageField(upload_to='pics', null=True)


class Comment (models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey (User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    date_published = models.DateField(auto_now=True)
    body = models.TextField (max_length=4000)
    #approve = models.IntegerField(null=True)

    #user_profile_image = models.ImageField()
    class Meta:
        db_table = 'comment_table'


#class Tags (models.Model) #? Remove tags in articles.
#class Approve (models.Model) #? Remove tags in articles.

# class User(models.Model):

#     id = models.BigAutoField(primary_key=True) # not in forms
#     first_name = models.CharField(max_length=30)
#     last_name= models.CharField(max_length=30)

#     username = models.CharField(max_length=30)
#     email = models.EmailField(max_length=30)
#     password=models.CharField(max_length=30)

#     short_description = models.TextField (max_length=160, blank=True)
#     long_description = models.TextField (max_length=1000, blank=True)