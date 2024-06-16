from django.shortcuts import render, get_object_or_404

from .models import Anime, Episode


def index(request):
    anime = Anime.objects.all()
    return render(request, 'index.html', {'anime': anime})


def view_anime(request, id):
    anime = get_object_or_404(Anime, id=id)
    episodes = Episode.objects.filter(anime=anime)
    return render(request, 'view.html', {'anime': anime})

