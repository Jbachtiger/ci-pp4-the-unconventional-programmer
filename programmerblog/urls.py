from django.urls import path
from .views import Home, PostDetail, CreatePost, EditPost

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('post/<slug:slug>', PostDetail.as_view(), name='post-detail'),
    path('create-post/', CreatePost.as_view(), name='create-post'),
    path('post/edit/<slug:slug>', EditPost.as_view(), name='edit-post'),
]