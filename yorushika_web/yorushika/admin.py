from django.contrib import admin
from .models import Overview, Album, Recommend, Song, Sanctuary


class RecommendAdmin(admin.ModelAdmin):
    list_display = ('id', 'song')
    list_display_links = ('id', 'song')


class OverviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


class SanctuaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'sanctuary')
    list_display_links = ('id', 'sanctuary')


admin.site.register(Recommend, RecommendAdmin)
admin.site.register(Overview, OverviewAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Sanctuary, SanctuaryAdmin)
