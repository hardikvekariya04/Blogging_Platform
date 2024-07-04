from django.contrib import admin
from comment.models import Comment
from ckeditor.widgets import CKEditorWidget
from django.db import models

# Change the Comment model view inside the admin panle
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'comment', 'created_at', 'updated_at')

# Register comment table on admin site
admin.site.register(Comment,CommentAdmin)