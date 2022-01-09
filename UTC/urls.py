from django.urls import path

from . import views

app_name = 'UTC'
urlpatterns = [
    # ex: /UTC/
    path('', views.index, name='index'),
    # ex: /UTC/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /UTC/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /UTC/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
