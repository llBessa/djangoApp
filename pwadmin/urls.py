from django.urls import path
from . import views

app_name="pwadmin"
urlpatterns = [
    path("", views.index, name="index")
]