from django.contrib import admin

from .models import CustomUser, FriendsList, WatchList, FavoriteList, AbandonedList, PlansList, Profile

admin.site.register(CustomUser)
admin.site.register(FriendsList)
admin.site.register(WatchList)
admin.site.register(AbandonedList)
admin.site.register(FavoriteList)
admin.site.register(PlansList)
admin.site.register(Profile)
