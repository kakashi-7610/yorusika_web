from django.urls import path
from . import views

app_name = 'yorushika'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('overview/', views.overview, name='overview'),
    path('recommend/', views.recommend, name='recommend'),
    path('album/', views.album, name='album'),
    path('sanctuary/', views.sanctuary, name='sanctuary'),
    path('song/<int:pk>/', views.song, name='song'),
]
