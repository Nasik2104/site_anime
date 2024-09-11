from django.urls import path

from . import views

app_name = 'anime'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('search', views.FindAnime.as_view(), name='search'),
    path('filter/<int:genre_id>', views.Index.as_view(), name='filter'),
    path('view/<int:pk>', views.AnimeDetail.as_view(), name='view'),
    path('watch_together/create/', views.CreateRoom.as_view(), name='create_room'),
    path('watch_together/watch/<int:pk>', views.WatchTogether.as_view(), name='watch_together'),
    path('add_to_list/<int:pk>', views.AddToList.as_view(), name='add_to_list')
]
