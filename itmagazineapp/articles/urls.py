from django.urls import path

from . import views

urlpatterns = [

    path("workspace/", views.workspace, name="workspace"),
    path("profile/", views.profile, name="profile"),
    path("" , views.home, name="home")

]