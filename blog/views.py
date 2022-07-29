from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
class PostView(generic.ListView):
    template_name = 'blog/posts.html'
    model = Post


class PostDetailView(generic.DetailView):
    template_name = 'blog/post.html'
    model = Post
