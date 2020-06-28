from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Post

def index(request):
    posts = Post.objects.order_by()
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}

    return render(request, 'blog/detail.html', context)