from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from rest_framework import routers
from api.views import OverviewViewSet, AlbumViewSet, SongViewSet, RecommendViewSet, SanctuaryViewSet, RecommendList
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


overview_router = routers.DefaultRouter()
overview_router.register('overview', OverviewViewSet)
album_router = routers.DefaultRouter()
album_router.register('album', AlbumViewSet)
song_router = routers.DefaultRouter()
song_router.register('song', SongViewSet)
recommend_router = routers.DefaultRouter()
recommend_router.register('recommend', RecommendViewSet)
sanctuary_router = routers.DefaultRouter()
sanctuary_router.register('sanctuary', SanctuaryViewSet)

app_name = 'api'
urlpatterns = [
    path('test/', views.sample, name='sample'),
    path('', include(overview_router.urls)),
    path('', include(album_router.urls)),
    # path('', include(song_router.urls)),
    # このURLを有効にするとrecommend/list/が使えなくなる。
    # path('', include(recommend_router.urls)),
    # path('', include(sanctuary_router.urls)),
    path('recommend/list/', views.recommend_list, name='recommend_list'),
    path('recommend/detail/<int:pk>/',
         views.recommend_detail, name='recommend_detail'),
    path('sanctuary/list/', views.sanctuary_list, name='sanctuary_list'),
    path('sanctuary/detail/<int:pk>/',
         views.sanctuary_detail, name='sanctuary_detail'),
    path('song/list/', views.song_list, name='song_list'),
    path('song/detail/<int:pk>/',
         views.song_detail, name='song_detail'),
    path('user/list/', views.user_list, name='user_list'),
    path('user/detail/<int:pk>/',
         views.user_detail, name='user_detail'),
]

# 例えば URL.jsonとしてするとjson形式で表示されるようになる
# urlpatterns = format_suffix_patterns(urlpatterns)
