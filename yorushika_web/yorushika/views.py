from django.shortcuts import render, get_object_or_404
from .models import Recommend, Overview, Album, Song, Sanctuary


def index(request):
    # -relese_datteにすると降順になる
    recommends = Recommend.objects.all().order_by('release_date')
    return render(request, 'yorushika/index.html', {"recommends": recommends})


def overview(request):
    overviews = Overview.objects.all().order_by('display_order')
    return render(request, 'yorushika/overview.html', {"overviews": overviews})


def recommend(request):
    # -relese_datteにすると降順になる
    recommends = Recommend.objects.all().order_by('release_date')
    return render(request, 'yorushika/recommend.html', {"recommends": recommends})


def album(request):
    # -relese_datteにすると降順になる
    albums = Album.objects.all().order_by('release_date')
    return render(request, 'yorushika/album.html', {"albums": albums})


def song(request, pk):
    # -relese_datteにすると降順になる
    albums = Album.objects.all().order_by('release_date')
    select_album = get_object_or_404(Album, pk=pk)
    songs = Song.objects.filter(
        album=select_album).order_by('song_order')
    return render(request, 'yorushika/song.html', {"songs": songs, "select_album": select_album, "albums": albums})


def sanctuary(request):
    # __modelで親のカラムを使用できる
    sanctuaries = Sanctuary.objects.all().order_by('song__album__release_date')
    return render(request, 'yorushika/sanctuary.html', {"sanctuaries": sanctuaries})
