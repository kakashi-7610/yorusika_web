from django.contrib import admin
from .models import Song, Overview


class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


class OverviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


admin.site.register(Song, SongAdmin)
admin.site.register(Overview, OverviewAdmin)
