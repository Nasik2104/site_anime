from django.contrib import admin

from .models import Anime, Episode, Genre, VoiceActingTeam, Room

admin.site.register(Anime)
admin.site.register(Episode)
admin.site.register(Genre)
admin.site.register(VoiceActingTeam)
admin.site.register(Room)
