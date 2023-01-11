from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # ex: /polls/5/
    path('question/<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('question/<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('question/<int:question_id>/vote/', views.vote, name='vote'),
]