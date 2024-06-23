from django.urls import path

from . import views

app_name = 'anime'

urlpatterns = [
    path('', views.index, name='index'),
    path('view/<int:anime_id>', views.view_anime, name='view'),
    path('add_episode/', views.add_episode, name='add_episode')
]
