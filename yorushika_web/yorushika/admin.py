from django.contrib import admin
from .models import Song


class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


admin.site.register(Song, SongAdmin)
