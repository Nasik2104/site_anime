from django.shortcuts import render, get_object_or_404, HttpResponse, redirect

from .models import Anime, Episode, VoiceActingTeam


def index(request):
    anime = Anime.objects.all()
    return render(request, 'index.html', {'anime': anime, 'title': 'Anima'})


def view_anime(request, anime_id):
    anime = get_object_or_404(Anime, id=anime_id)
    episodes = Episode.objects.filter(anime=anime)
    return render(request, 'view.html', {'anime': anime, 'title': anime.name})


def add_episode(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        video = request.FILES.get('video')
        anime_id = request.POST.get('anime')
        team_id = request.POST.get('voice_acting_team')

        try:
            anime = Anime.objects.get(id=anime_id)
            team = VoiceActingTeam.objects.get(id=team_id)
            new_episode = Episode(name=name, video=video, anime=anime, voice_acting_team=team)
            new_episode.full_clean()
            new_episode.save()
        except Anime.DoesNotExist:
            return HttpResponse('Invalid anime selected.')
        except VoiceActingTeam.DoesNotExist:
            return HttpResponse('Invalid voice acting team selected.')
        except Exception as e:
            return HttpResponse(f'Error: {str(e)}')
        else:
            return redirect('anime:index')

    animes = Anime.objects.all()
    teams = VoiceActingTeam.objects.all()

    return render(request, 'add_episode.html', {'animes': animes, 'teams': teams})
