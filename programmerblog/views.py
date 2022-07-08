from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy 
from .models import Post
from .forms import PostForm, EditForm


class Home(generic.ListView):
    model = Post
    template_name = 'home.html'
    paginate_by = 20


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_details.html'


class CreatePost(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create_post.html'


class EditPost(generic.UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit_post.html'
    


class DeletePost(generic.DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    