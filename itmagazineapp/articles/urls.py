from django.urls import path 

from . import views

urlpatterns = [

    path("" , views.home, name="home"),

    path("signup/", views.sign_up, name="signup"),
    path("workspace/", views.workspace, name="workspace"),

    path("article/<int:article_id>/", views.article, name="article"),
    path("editarticle/<int:article_id>/", views.edit_article, name="editarticle"),

    path("user/<int:user_id>/", views.user, name="user"),
    path("edituser/<int:user_id>/", views.edit_user, name="edituser"),
    

]