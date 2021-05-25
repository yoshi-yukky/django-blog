from django.urls import path

from . import views

urlpatterns = [
    path("", views.BlogListView.as_view(), name="blog-index"),
    path("<int:pk>/", views.BlogDetailView.as_view(), name="blog-detail"),
]
