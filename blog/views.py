from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.

class WriteView(generic.CreateView):
    template_name = 'blog/post_new.html'
    model = Post
    fields = ['title', 'author', 'text']

    def get_initial(self,):
        initial = super().get_initial()
        initial['author'] = self.request.user.get_username()
        return initial


class PostView(generic.ListView):
    template_name = 'blog/posts.html'
    model = Post

class PostDetailView(generic.DetailView):
    template_name = "blog/post.html"
    model = Post
