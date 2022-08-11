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
    path('mypage/<int:pk>/', views.mypage, name='mypage'),
    path('login/', auth_views.LoginView.as_view(template_name='yorushika/login.html'), name='login'),
    path('mypage/<int:pk>/detail/', views.mypage_detail, name='mypage_detail'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('recommend/new/', views.recommend_new, name='recommend_new'),
    path('recommend/<int:pk>/detail/',
         views.recommend_detail, name='recommend_detail'),
    path('recommend/<int:pk>/update/',
         views.recommend_update, name='recommend_update'),
    path('recommend/<int:pk>/delete/',
         views.recommend_delete, name='recommend_delete'),
]
