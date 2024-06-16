from django.db import models


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
    added_at = models.DateTimeField(auto_now_add=True)
    genres = models.ManyToManyField(Genre)
    voices = models.ManyToManyField(VoiceActingTeam)
    episodes_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='anime_images/')

    def __str__(self):
        return self.name

    def get_episodes_voiced_count(self):
        return self.episodes.count()


class Episode(models.Model):
    name = models.CharField(max_length=32)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    video = models.FileField(upload_to='episodes/')
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='episodes')
    voice_acting_team = models.ForeignKey(VoiceActingTeam, on_delete=models.CASCADE, related_name='episodes')

    def __str__(self):
        return self.name
