from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Main web app
    path('health/', views.health_check, name='health_check'),
    path('movies/', views.get_movies, name='get_movies'),
    path('search/', views.search_movies, name='search_movies'),
    path('recommend/', views.get_recommendations, name='get_recommendations'),
    path('movie/<str:movie_title>/', views.get_movie_details, name='get_movie_details'),
]
