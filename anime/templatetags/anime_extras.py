from django import template
from anime.models import Anime

register = template.Library()


@register.simple_tag
def get_recent_updates():
    return Anime.objects.all().order_by('-added_at')[:5]
