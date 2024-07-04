from rest_framework import serializers
from .models import Post

# Serializer for reading Post objects.
class PostReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

# Serializer for writing (creating and updating) Post objects.
class PostWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
    
    def validate(self, data):
        # Get the title and user from the data
        title = data.get('title')
        author = self.context['request'].user

        # Check if a post with the same title by the same author already exists
        if Post.objects.filter(title=title, author=author).exists():
            raise serializers.ValidationError("You have already created a post with this title.")

        return data
