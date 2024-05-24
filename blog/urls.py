from django.urls import path
from .views import PostListView, PostDetailView, HomePageView,TaggedPostListView

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('tag/<slug:tag_slug>/', TaggedPostListView.as_view(), name='tagged_post_list'),
]
