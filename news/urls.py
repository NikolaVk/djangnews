from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('searchResults', views.searchResults, name='searchResults'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),

]
