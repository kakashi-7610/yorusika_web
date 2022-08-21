from django.shortcuts import render, redirect, get_object_or_404
from .models import Recommend, Overview, Album, Song, Sanctuary
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import RecommendForm
from django.views.decorators.http import require_POST


def index(request):
    # -relese_datteにすると降順になる
    recommends = Recommend.objects.all().order_by('-created_at')
    return render(request, 'yorushika/index.html', {"recommends": recommends})


def overview(request):
    overviews = Overview.objects.all().order_by('display_order')
    return render(request, 'yorushika/overview.html', {"overviews": overviews})


def recommend(request):
    # -relese_datteにすると降順になる
    recommends = Recommend.objects.all().order_by('-created_at')
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


def mypage(request, pk):
    user = get_object_or_404(User, pk=pk)
    # user.photo_set.all()でユーザーに紐づく曲を取得
    recommends = user.recommend_set.all().order_by('-created_at')
    contents = {
        "user": user,
        "recommends": recommends,
    }
    return render(request, 'yorushika/mypage.html', contents)


@login_required
def mypage_detail(request, pk):
    recommend = get_object_or_404(Recommend, pk=pk)
    # サイドメニューにてリストを表示するためユーザーに紐づくrecommendを取得
    recommends = Recommend.objects.filter(
        user=recommend.user).order_by('-created_at')
    contents = {
        'recommend': recommend,
        'recommends': recommends,
        'menu_title': 'LIST',
        'link': 'mypage',
    }
    return render(request, 'yorushika/recommend_detail.html', contents)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            input_username = form.cleaned_data['username']
            input_password = form.cleaned_data['password1']
            # フォームの入力値で認証で切ればユーザーオブジェクト、できなければNoneを返す
            new_user = authenticate(
                username=input_username,
                password=input_password,
            )
            # 認証成功時のみ、ユーザーをログインさせる
            if new_user is not None:
                # login関数は、認証ができてなくてもログインさせることができる。(認証は上のauthenticateで実⾏する)
                login(request, new_user)
                return redirect('yorushika:mypage', pk=new_user.pk)
    else:
        form = UserCreationForm()
    return render(request, 'yorushika/signup.html', {'form': form})


# ログインしていないユーザーはLOGIN_URLにリダイレクトする
@login_required
def recommend_new(request):
    if request.method == "POST":
        form = RecommendForm(request.POST)
        if form.is_valid():
            recommend = form.save(commit=False)
            recommend.user = request.user
            recommend.save()
        return redirect('yorushika:mypage', pk=request.user.pk)
    else:
        form = RecommendForm()
        return render(request, 'yorushika/recommend_new.html', {'form': form})


def recommend_detail(request, pk):
    recommend = get_object_or_404(Recommend, pk=pk)
    # サイドメニューにてリストを表示するためユーザーに紐づくrecommendを取得
    recommends = Recommend.objects.all().order_by('-created_at')[:10]
    contents = {
        'recommend': recommend,
        'recommends': recommends,
        'menu_title': '最新10件',
        'link': 'recommend',
    }
    return render(request, 'yorushika/recommend_detail.html', contents)


@login_required
def recommend_update(request, pk):
    recommend = get_object_or_404(Recommend, pk=pk, user=request.user)
    if request.method == "POST":
        # instanceを指定することで元の値を埋め込める
        form = RecommendForm(request.POST, instance=recommend)
        if form.is_valid():
            form.save()
            return redirect('yorushika:mypage', request.user.id)
    else:
        # instanceを指定することで元の値を埋め込める
        form = RecommendForm(instance=recommend)
        return render(request, 'yorushika/recommend_update.html', {'recommend': recommend, 'form': form})


@require_POST
def recommend_delete(request, pk):
    recommend = get_object_or_404(Recommend, pk=pk, user=request.user)
    recommend.delete()
    return redirect('yorushika:mypage', request.user.id)
