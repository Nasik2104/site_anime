from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from .models import Anime, Episode, VoiceActingTeam, Room
from .forms import CreateRoomForm


class Index(ListView):
    model = Anime
    template_name = 'anime/index.html'
    context_object_name = 'anime'


class FindAnime(ListView):
    model = Anime
    template_name = 'anime/index.html'
    context_object_name = 'anime'

    def get_queryset(self):
        return Anime.objects.search(self.request.GET.get('q'))


class EpisodeDetail(DetailView):
    model = Anime
    template_name = 'anime/view.html'
    context_object_name = 'anime'


class CreateRoom(CreateView, LoginRequiredMixin):
    model = Room
    template_name = 'anime/create_room.html'
    form_class = CreateRoomForm

    def form_valid(self, form):
        form.instance.admin_id = self.request.user.id
        return super().form_valid(form)

    def get_success_url(self):
        room_id = self.object.id
        return reverse_lazy('anime:watch_together', kwargs={'pk': room_id})


class WatchTogether(DetailView):
    model = Room
    template_name = 'anime/watch_together.html'

