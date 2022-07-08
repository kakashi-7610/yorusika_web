from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'yorushika'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('overview/', views.overview, name='overview'),
    path('recommend/', views.recommend, name='recommend'),
    path('album/', views.album, name='album'),
    path('sanctuary/', views.sanctuary, name='sanctuary'),
    path('song/<int:pk>/', views.song, name='song'),
    path('mypage/', views.mypage, name='mypage'),
    path('users/<int:pk>/', views.users, name='users'),
    path('login/', auth_views.LoginView.as_view(template_name='yorushika/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
