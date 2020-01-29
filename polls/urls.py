from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # In Tutoral 4 change the view.index or views.detail like views.IndexView.as_view() and after dataType in <int:question_id> changes with pk which is primany key in Django
    # for /polls/
    path('', views.IndexView.as_view(), name='index'),
    # for /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # for /polls/5/result/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # for /polls/5/vote/
    path('<int:pk>/vote/', views.vote, name='vote'),
]
