from django.urls import path
from . import views

app_name="pwadmin"
urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("login/handle_login/", views.handle_login, name="handle_login"),
    path("passwords/", views.passwords, name="passwords")
]