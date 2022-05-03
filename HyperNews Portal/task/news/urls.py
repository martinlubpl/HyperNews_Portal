from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('news/<int:link_id>/', views.news, name='news_detail'),
    path('news/', views.news, name='all news'),
]
