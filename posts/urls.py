from django.contrib import admin
from django.urls import path, include
from .views import (
    ListPosts,
    PostDetail,
    CommentLike,
    CommentDislike,
    CreatePost,
    DeletePost
)

urlpatterns = [
    path("<int:spaceid>/", ListPosts.as_view(), name="posts"),
    path("postdetail/<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("like/<int:pk>/", CommentLike.as_view(), name="comment_like"),
    path("dislike/<int:pk>/", CommentDislike.as_view(), name="comment_dislike"),
    path("create-post/<int:spaceid>/", CreatePost.as_view(), name="create_post"),
    path("delete-post/<int:pk>/", DeletePost.as_view(), name="delete_post"),
]
