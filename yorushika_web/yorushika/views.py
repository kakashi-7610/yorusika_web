from django.shortcuts import render
from .models import Song


def index(request):
    # -relese_datteにすると降順になる
    songs = Song.objects.all().order_by('release_date')
    return render(request, 'yorushika/index.html', {"songs": songs})


def overview(request):
    return render(request, 'yorushika/overview.html')


def recommend(request):
    return render(request, 'yorushika/recommend.html')


def album(request):
    return render(request, 'yorushika/album.html')


def sanctuary(request):
    return render(request, 'yorushika/sanctuary.html')
