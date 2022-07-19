''' Imports ''' 
from django.shortcuts import redirect, reverse, get_object_or_404
from django.views import generic, View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import PostForm, EditForm, CommentForm


class Home(generic.ListView):
    ''' Class to show all posts in a list view on homepage '''
    model = Post
    template_name = 'home.html'
    paginate_by = 20


class PostDetail(generic.DetailView):
    ''' Class to show single posts in a detail view '''
    model = Post
    template_name = 'post_details.html'

    form = CommentForm

    def post(self, request, *args, **kwargs):
        ''' Get the post by slug, validates comment form and redirects to post-detail page '''
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse("post-detail", kwargs={
                'slug': post.slug
            }))

    def get_context_data(self, **kwargs):
        ''' Display comment form and likes '''
        liked = False
        post = get_object_or_404(Post, slug=self.object.slug)
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        post_comments_count = Comment.objects.all().filter(post=self.object.id).count()
        post_comments = Comment.objects.all().filter(post=self.object.id)
        context = super().get_context_data(**kwargs)
        context.update({
            'liked': liked,
            'form': self.form,
            'post_comments': post_comments,
            'post_comments_count': post_comments_count,
        })

        return context


class PostLike(View):
    ''' Class to allow liking funcitionality and redirect 
        to post-detail page on like submit 
    '''
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post-detail', args=[slug]))


class CreatePost(generic.CreateView):
    ''' Class to allow posts to be created '''
    model = Post
    form_class = PostForm
    template_name = 'create_post.html'


class EditPost(generic.UpdateView):
    ''' Class to allow posts to be edited '''
    model = Post
    form_class = EditForm
    template_name = 'edit_post.html'
    


class DeletePost(generic.DeleteView):
    ''' Class to allow posts to be deleted '''
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    