from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Post
from .serializers import PostReadSerializer, PostWriteSerializer
from .permission import IsAuthorOrReadOnly

# PostListView Creating and display all the blog posts
class PostListView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """Retrieve all posts."""
        query_params = request.query_params
        title = query_params.get('title', None)
        
        posts = Post.objects.all()

        # Added search functionality
        if title:
            filtered_posts = []
            for post in posts:
                if title.lower() in post.title.lower():
                    filtered_posts.append(post)
            posts = filtered_posts

        serializer = PostReadSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Create a new post."""
        serializer = PostWriteSerializer(data=request.data, context={'request': request})
        
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response({'message': 'Post added successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# PostDetailView displays, edits, and deletes a specific blog post.  
class PostDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        """Retrieve a specific post."""
        try:
            post = Post.objects.get(id=pk)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PostReadSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        """Update a specific post."""
        print(request.data)
        try:
            post = Post.objects.get(id=pk)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
        self.check_object_permissions(request, post)
        serializer = PostWriteSerializer(post, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Post updated successfully', 'data': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        """Partially update a specific post."""
        try:
            post = Post.objects.get(id=pk)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
        self.check_object_permissions(request, post)
        serializer = PostWriteSerializer(post, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Post partially updated successfully', 'data': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete a specific post."""
        try:
            post = Post.objects.get(id=pk)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
        self.check_object_permissions(request, post)
        post.delete()
        return Response({'message': 'Post deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

    def get_permissions(self):
        """Set permissions based on request method."""
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            self.permission_classes = [IsAuthorOrReadOnly]
        elif self.request.method == "POST":
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [AllowAny]
        return super().get_permissions()

