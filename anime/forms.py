from django import forms

from .models import Episode, Room, VoiceActingTeam, Anime


class VoiceForm(forms.ModelForm):
    class Meta:
        model = VoiceActingTeam
        fields = ['name']


class EpisodeForm(forms.ModelForm):
    class Meta:
        model = Episode
        fields = ['name', 'number', 'video', 'voice_acting_team', 'anime']

        labels = {
            'name': 'Назва серії',
            'number': 'Номер серії',
            'voice_acting_team': 'Команда озвучування(якщо немає додайте)',
            'anime': 'Аніме',
            'video': 'Епізод'
        }


class CreateRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['anime', 'episode']

        labels = {
            'anime': 'Аніме',
            'episode': 'Епізод'
        }

        widgets = {
            'admin_id': forms.HiddenInput()
        }
