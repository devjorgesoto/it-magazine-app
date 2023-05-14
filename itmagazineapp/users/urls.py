from django.urls import path 

from . import views

# app url path ./users/...

urlpatterns = [

    #path("" , views.home, name="home"),
    path("user/<int:user_id>/", views.user, name="user"),
    path("edituser/<int:user_id>/", views.edit_user, name="edituser"),
    path("signup/", views.sign_up, name="signup"),
    
]