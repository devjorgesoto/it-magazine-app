from django.urls import path 

from . import views

urlpatterns = [

    path("" , views.home, name="home"), # should this go in itmagazine app?

    path("workspace/", views.workspace, name="workspace"),
    path("article/<int:article_id>/", views.article, name="article"),
    path("editarticle/<int:article_id>/", views.edit_article, name="editarticle"),

]