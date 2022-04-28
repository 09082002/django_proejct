from django.urls import path
from .import views
from .views import RegisterUser, LoginUser, logout_user
from .views import *





urlpatterns = [
    path('', views.about, name='/'),
    path('about/', views.index, name='about'),
    path('home/', views.home, name='home'),
    path('travel/', views.travel, name='travel'),
    path('games/', views.games, name='games'),
    path('tours/', views.tours, name='tours'),
    path('base/', views.base, name='base'),
    path('foods/', views.foods, name='foods'),
    path('create/', views.create, name='create'),
    path('culture/', views.culture, name='culture'),
    path('news_home/', views.news_home, name='news_home'),
    # path('register_user/', views.register_user, name='register_user'),
    path('send/', sends_message),
    # path('information/', views.info, name='info'),
    # path('userinfo', views.userinfo, name='userinfo'),
    # path('post/<slug:post_slug>', views.show_post, name='post'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('sends/', EmailAttachementView.as_view(), name='emailattachment'),

    path('addpage/', views.addpage, name='addpage'),
    path('news_home/<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('news_home/<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),
    # path('news_home/<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete'),
    path('registration_done/', views.done, name='register_done'),
]
