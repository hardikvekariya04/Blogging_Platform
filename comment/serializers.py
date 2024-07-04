from rest_framework import serializers
from .models import Comment

# Serializer for reading Comment objects.
class CommentReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

# Serializer for writing Comment objects.
class CommentWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment']