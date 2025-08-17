from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.

class PostList(generic.ListView):
    # model = Post  #a collectionof all posts = Post.objects.all()
    queryset = Post.objects.filter(status=1)  # Only show published posts
    template_name = 'blog/index.html'
    paginate_by = 6
