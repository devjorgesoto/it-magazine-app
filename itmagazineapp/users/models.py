from django.db import models

class User(models.Model):

    id = models.BigAutoField(primary_key=True) 
    first_name = models.CharField(max_length=30)
    last_name= models.CharField(max_length=30)

    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password=models.CharField(max_length=30)

    short_description = models.TextField (max_length=160, blank=True)
    long_description = models.TextField (max_length=1000, blank=True)

    class Meta:
        db_table = 'user_table'
 