from django.contrib import admin
from .models import Overview, Album, Recommend


class RecommendAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


class OverviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


admin.site.register(Recommend, RecommendAdmin)
admin.site.register(Overview, OverviewAdmin)
admin.site.register(Album, AlbumAdmin)
