from django.contrib import admin
from django.urls import path
from comment.views import CommentListView, CommentDetailView


urlpatterns = [
    path('post/comment/', CommentListView.as_view(), name='comment'),
    path('post/<int:post_id>/comment/', CommentListView.as_view(), name='commentlistview'),
    path('post/<int:post_id>/comment/<int:pk>/', CommentDetailView.as_view(), name='commentdetailview'),
]

