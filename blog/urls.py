from django.urls import path,include
from . import views
from . views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
urlpatterns = [
    path('',PostListView.as_view(),name="blog-home"),
    path('post-detail/<int:pk>/',PostDetailView.as_view(),name="post-detail"),
    path('post-create',PostCreateView.as_view(),name="post-create"),
    path('post-update/<int:pk>/',PostUpdateView.as_view(),name="post-update"),
    path('post-delete/<int:pk>/',PostDeleteView.as_view(),name="post-delete"),
    path('user-posts/<str:username>',UserPostListView.as_view(),name="user-posts"),
]