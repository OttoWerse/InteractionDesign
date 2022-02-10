from django.urls import path

from . import views

app_name = 'UTC'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('form/', views.FormVIew.as_view(), name='form'),
    path('schottland/', views.SchottlandView.as_view(), name='schottland'),
    path('indien/', views.IndienView.as_view(), name='indien'),
    path('georgien-armenien/', views.GeorgienArmenienView.as_view(), name='georgien-armenien'),
    path('tansania/', views.TansaniaView.as_view(), name='tansania'),
    path('norwegen/', views.NorwegenView.as_view(), name='norwegen'),
    path('hawaii/', views.HawaiiView.as_view(), name='hawaii'),
    path('alaska/', views.AlaskaView.as_view(), name='alaska'),
    path('island/', views.IslandView.as_view(), name='island'),
    path('registered/', views.registered, name='registered'),
]
