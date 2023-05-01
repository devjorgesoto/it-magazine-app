from django.db import models

class User(models.Model):

    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name= models.CharField(max_length=30)

    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password=models.CharField(max_length=30)

    short_description = models.TextField (blank=True, max_length=160)
    long_description = models.TextField (blank=True, max_length=1000)
 

class Article (models.Model):

    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey (User, on_delete=models.CASCADE)

    headline = models.TextField(max_length=60)
    description = models.TextField (max_length=160)
    body = models.TextField (max_length=4000)




