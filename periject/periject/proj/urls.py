from django.conf.urls import url
from django.contrib.auth import views as auth_views
from periject.account import views
from django.urls import path
from . import views


urlpatterns = [
    
    url(r'^newproject/$',views.CreateNewProject.as_view(),name='newproject'),
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    ]
