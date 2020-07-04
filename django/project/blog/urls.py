from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog-index'),
    path('<int:pk>/', views.BlogDetail.as_view(), name='blog-detail'),
    path('category/<int:pk>/', views.BlogCategory.as_view(), name='blog-category'),
]