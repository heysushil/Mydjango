from django.urls import path
from . import views

urlpatterns = [
    # for /polls/
    path('', views.index, name='index'),
    # for /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # for /polls/5/result/
    path('<int:question_id>/results/', views.results, name='results'),
    # for /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
