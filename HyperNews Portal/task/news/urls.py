from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('news/<int:link_id>/', views.news, name='news_detail'),
    path('news/', views.news, name='all news'),
    path('news/create/', views.CreateNews.as_view(), name='create_news'),

]
urlpatterns += static(settings.STATIC_URL)