from django.shortcuts import render
from django.views import generic
from .models import Post


class Home(generic.ListView):
    model = Post
    template_name = 'home.html'
    paginate_by = 20


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_details.html'


class CreatePost(generic.CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = ('title', 'author', 'title_tag', 'hero_image', 'body', 'topic')

