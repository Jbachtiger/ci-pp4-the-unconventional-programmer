from django.urls import path
from .views import Home, PostDetail, CreatePost

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('posts/<int:pk>', PostDetail.as_view(), name='post-detail'),
    path('create-post/', CreatePost.as_view(), name='create-post')
]