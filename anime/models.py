from django.db import models

from users.models import CustomUser


class AnimeManager(models.Manager):
    def search(self, data):
        return self.filter(name__icontains=data)


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class VoiceActingTeam(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Anime(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    year = models.IntegerField()
    studios = models.CharField(max_length=128)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    genres = models.ManyToManyField(Genre)
    voices = models.ManyToManyField(VoiceActingTeam)
    episodes_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='anime_images/')
    views = models.IntegerField(default=0)

    objects = AnimeManager()

    def __str__(self):
        return self.name

    def get_episodes_voiced_count(self):
        return self.episodes.aggregate(models.Max('number'))['number__max']


class Episode(models.Model):
    name = models.CharField(max_length=32)
    number = models.IntegerField()
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    video = models.FileField(upload_to='episodes/')
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='episodes')
    voice_acting_team = models.ForeignKey(VoiceActingTeam, on_delete=models.CASCADE, related_name='episodes')

    def __str__(self):
        return self.name


class Room(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
    admin = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_room')
    watchers = models.ManyToManyField(CustomUser, related_name='room')

    def __str__(self):
        return f"{self.anime.name} {self.episode.number} {self.id}"
