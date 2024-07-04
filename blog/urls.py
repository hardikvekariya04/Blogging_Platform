from django.contrib import admin
from django.urls import path
from blog.views import PostListView, PostDetailView


urlpatterns = [
    path('post/', PostListView.as_view(), name='postlistview'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='postdetailview'),
]

