from django.urls import path

from . import views

urlpatterns = [

    # Remember: Every path here have "articles/" added before.

    path( "" , views.home, name="home"),
    path( "article/" , views.article, name="article"),

]