from django.urls import path

from . import views

urlpatterns = [
    path("", views.BlogListView.as_view(), name="blog_index"),
    path("category/<str:name>/", views.BlogListByFilteredCategoryView.as_view(), name="blog_category"),
    path("<int:pk>/", views.BlogDetailView.as_view(), name="blog_detail"),
]
