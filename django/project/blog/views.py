from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic

from .models import Post, Category


class BlogMixin(generic.base.ContextMixin):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context

class BlogList(BlogMixin, generic.ListView):
    template_name = "blog/list.html"
    model = Post
    ordering = ['-created_at']
    paginate_by = 5

class BlogDetail(BlogMixin, generic.DetailView):
    template_name = "blog/detail.html"
    model = Post

class BlogCategory(BlogMixin, generic.DetailView):
    template_name = "blog/list.html"
    model = Post
    ordering = ['-created_at']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data_list = Post.objects.filter(category=self.kwargs['pk'])
        context['object_list'] = data_list
        return context