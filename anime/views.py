from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404

from .models import Anime, Room, Genre
from .forms import CreateRoomForm, ChooseListForm

from users.models import ListManager


class Index(ListView):
    model = Anime
    template_name = 'anime/index.html'
    context_object_name = 'anime'
    paginate_by = 10

    def get_queryset(self):
        anime = Anime.objects.all()
        genre_id = self.kwargs.get('genre_id')

        if genre_id:
            genre = get_object_or_404(Genre, id=genre_id)
            anime = anime.filter(genres=genre)

        return anime

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class FindAnime(ListView):
    model = Anime
    template_name = 'anime/index.html'
    context_object_name = 'anime'
    paginate_by = 10

    def get_queryset(self):
        return Anime.objects.search(self.request.GET.get('q'))


class AnimeDetail(DetailView):
    model = Anime
    template_name = 'anime/view.html'
    context_object_name = 'anime'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_list_name = ListManager().get_anime_list(Anime.objects.get(id=self.kwargs.get("pk")), self.request.user)
        form = ChooseListForm(initial={'list': current_list_name})
        context['form'] = form
        return context


class AddToList(CreateView):
    def post(self, request, pk):
        form = ChooseListForm(request.POST)
        if form.is_valid():
            list_name = form.cleaned_data['list']
            anime = get_object_or_404(Anime, pk=pk)
            user = request.user

            ListManager().add(list_name, anime, user)

            return redirect('anime:view', pk=pk)
        return redirect('anime:view', pk=pk)


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


class WatchTogether(DetailView, LoginRequiredMixin):
    model = Room
    template_name = 'anime/watch_together.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.update_data()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def update_data(self):
        if self.request.user not in self.object.watchers.all():
            self.object.watchers.add(self.request.user)

