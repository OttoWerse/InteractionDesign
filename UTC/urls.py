from django.urls import path

from . import views

app_name = 'UTC'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('form/', views.FormVIew.as_view(), name='form'),
    path('island/', views.IslandView.as_view(), name='island'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]
