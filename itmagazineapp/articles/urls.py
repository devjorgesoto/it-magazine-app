from django.urls import path

from . import views

urlpatterns = [

    path("signup/", views.sign_up, name="signup"),
    path("read/<int:article_id>", views.read, name="read"),
    path("workspace/", views.workspace, name="workspace"),
    path("profile/<int:user_id>", views.profile, name="profile"),
    path("" , views.home, name="home")

]