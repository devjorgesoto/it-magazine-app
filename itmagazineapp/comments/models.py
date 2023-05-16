from django.db import models
from users.models import User
from articles.models import Article

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
