from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("signup/", views.sign_up, name="signup"),
    path("basic-user-details/", views.GetBasicUserDetails, name="basic_user_details")
]
