from django.db import models

class Writer(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_last= models.CharField(max_length=30)
    short_description = models.CharField (max_length=160)
    long_description = models.CharField (max_length=450)

class Reader(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_last= models.CharField(max_length=30)
    short_description = models.CharField (max_length=160)
    long_description = models.CharField (max_length=450)

class Article (models.Model):
    id = models.BigAutoField(primary_key=True)
    writer = models.ForeignKey (Writer, on_delete=models.CASCADE)
    headline = models.CharField(max_length=60)
    description = models.CharField (max_length=160)
    body = models.CharField (max_length=2000)



