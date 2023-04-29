from django.urls import path

from . import views

urlpatterns = [

    # Remember: Every path here have "articles/" added before.

    path("register_result/", views.register_result, name="register_result"),
    path("" , views.home, name="home"),

]