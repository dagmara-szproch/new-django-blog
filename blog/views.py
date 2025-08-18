from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

# Create your views here.

class PostList(generic.ListView):
    # model = Post  #a collectionof all posts = Post.objects.all()
    queryset = Post.objects.filter(status=1)  # Only show published posts
    template_name = 'blog/index.html'
    paginate_by = 6

# Display an individual post
# This function is used to display a single post based on its slug.
# The slug is a unique identifier for the post, typically derived from the post's title.
# It allows for cleaner URLs and better SEO.
def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )

# another way using when you have a lot of items in context
# def post_detail(request, slug):

#     queryset = Post.objects.filter(status=1)
#     post = get_object_or_404(queryset, slug=slug)

#     context = {"post": post}

#     return render(
#         request,
#         "blog/post_detail.html",
#         context
#     )