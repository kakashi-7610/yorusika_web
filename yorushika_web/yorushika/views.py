from django.shortcuts import render


def index(request):
    return render(request, 'yorushika/index.html')


def overview(request):
    return render(request, 'yorushika/overview.html')


def recommend(request):
    return render(request, 'yorushika/recommend.html')


def album(request):
    return render(request, 'yorushika/album.html')


def sanctuary(request):
    return render(request, 'yorushika/sanctuary.html')
