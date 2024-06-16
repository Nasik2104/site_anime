from django.urls import path

from . import views

app_name = 'anime'

urlpatterns = [
    path('', views.index, name='index'),
    path('view/<int:id>', views.view_anime, name='view')
]
