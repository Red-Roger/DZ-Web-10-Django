from django.urls import path
from . import views

app_name = 'quoteapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('author/Albert Einstein.html', views.AlbertEinstein, name='AlbertEinstein'),
    path('author/J.K. Rowling.html', views.JKRowling, name='JKRowling'),
    path('author/Jane Austen.html', views.JaneAusten, name='JaneAusten'),
    path('author/Thomas Mann.html', views.ThomasMann, name='ThomasMann'),
    path('author/Marilyn Monroe.html', views.MarilynMonroe, name='MarilynMonroe'),
    path('author/André Gide.html', views.AndréGide, name='AndréGide'),
    path('author/Thomas A. Edison.html', views.ThomasAEdison, name='ThomasAEdison'),
    path('author/Eleanor Roosevelt.html', views.EleanorRoosevelt, name='EleanorRoosevelt'),
    path('author/Steve Martin.html', views.SteveMartin, name='SteveMartin'),
]