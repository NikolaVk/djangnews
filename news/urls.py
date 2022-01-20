from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('searchResults', views.searchResults, name='searchResults'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('tech', views.tech, name='tech'),
    path('world', views.world, name='world'),
    path('sport', views.sport, name='sport'),
    path('business', views.business, name='business'),
    path('travel', views.travel, name='travel'),
    path('media', views.media, name='media'),
    path('breaking', views.breaking, name='breaking'),
]
