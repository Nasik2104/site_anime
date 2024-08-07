from django.urls import path

from . import views

app_name = 'anime'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('search', views.FindAnime.as_view(), name='search'),
    path('view/<int:pk>', views.EpisodeDetail.as_view(), name='view'),
    path('watch_together/create/', views.CreateRoom.as_view(), name='create_room'),
    path('watch_together/watch/<int:pk>', views.WatchTogether.as_view(), name='watch_together')
    # path('add_episode/', views.add_episode, name='add_episode')
]
