from django.shortcuts import render
from .models import Recommend, Overview


def index(request):
    # -relese_datteにすると降順になる
    recommends = Recommend.objects.all().order_by('release_date')
    return render(request, 'yorushika/index.html', {"recommends": recommends})


def overview(request):
    overviews = Overview.objects.all().order_by('created_at')
    return render(request, 'yorushika/overview.html', {"overviews": overviews})


def recommend(request):
    # -relese_datteにすると降順になる
    recommends = Recommend.objects.all().order_by('release_date')
    return render(request, 'yorushika/recommend.html', {"recommends": recommends})


def album(request):
    return render(request, 'yorushika/album.html')


def sanctuary(request):
    return render(request, 'yorushika/sanctuary.html')
