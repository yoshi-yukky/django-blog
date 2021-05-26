from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.db.models import Count, Prefetch
from blog.models import Post, Category
from common.decorators import disable_side_bar


class BlogContextMixin(generic.base.ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = Category.objects.prefetch_related(
            Prefetch("post_set", queryset=Post.objects.all(), to_attr="prefetched_post")
        )
        context["categories"] = qs.all()
        return context


class BlogListView(generic.ListView, BlogContextMixin):
    template_name = "blog/list.html"
    model = Post
    queryset = Post.objects.select_related("category")
    ordering = ["-created_at"]
    paginate_by = 5


class BlogListByFilteredCategoryView(BlogListView):
    def get_queryset(self):
        category_name = self.kwargs["name"]
        return Post.objects.filter(category__name=category_name).select_related("category")


@disable_side_bar
class BlogDetailView(generic.DetailView, BlogContextMixin):
    template_name = "blog/detail.html"
    model = Post
