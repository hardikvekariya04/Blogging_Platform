from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Post, Comment
from .serializers import CommentReadSerializer, CommentWriteSerializer
from blog.permission import IsAuthorOrReadOnly

# CommentListView Creating and display all the comment of blog posts
class CommentListView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, post_id=None):
        """Retrieve comments for a specific post or all comments."""
        if post_id is None:
            comments = Comment.objects.all()
        else:
            comments = Comment.objects.filter(post__id=post_id)
        serializer = CommentReadSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, post_id):
        """Create a new comment for a specific post."""
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CommentWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user, post=post)
            return Response({'message': 'Comment created successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# CommentDetailView displays, edits, and deletes a specific blog post comment.  
class CommentDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, post_id, pk):
        """Retrieve a specific comment."""
        try:
            comment = Comment.objects.get(post_id=post_id, id=pk)
        except Comment.DoesNotExist:
            return Response({'error': 'Comment not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CommentReadSerializer(comment)
        return Response(serializer.data)

    def put(self, request, post_id, pk):
        """Update a specific comment."""
        try:
            comment = Comment.objects.get(post_id=post_id, id=pk)
        except Comment.DoesNotExist:
            return Response({'error': 'Comment not found'}, status=status.HTTP_404_NOT_FOUND)
        self.check_object_permissions(request, comment)
        serializer = CommentWriteSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Comment updated successfully', 'data': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, post_id, pk):
        """Partially update a specific comment."""
        try:
            comment = Comment.objects.get(post_id=post_id, id=pk)
        except Comment.DoesNotExist:
            return Response({'error': 'Comment not found'}, status=status.HTTP_404_NOT_FOUND)
        self.check_object_permissions(request, comment)
        serializer = CommentWriteSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Comment partially updated successfully', 'data': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_id, pk):
        """Delete a specific comment."""
        try:
            comment = Comment.objects.get(post_id=post_id, id=pk)
        except Comment.DoesNotExist:
            return Response({'error': 'Comment not found'}, status=status.HTTP_404_NOT_FOUND)
        self.check_object_permissions(request, comment)
        comment.delete()
        return Response({'message': 'Comment deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

    def get_permissions(self):
        """Set permissions based on request method."""
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            self.permission_classes = [IsAuthorOrReadOnly]
        elif self.request.method == "POST":
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [AllowAny]
        return super().get_permissions()
