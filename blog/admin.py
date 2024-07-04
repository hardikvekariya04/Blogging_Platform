from django.contrib import admin
from blog.models import Post
from ckeditor.widgets import CKEditorWidget
from django.db import models

# Change the Post model view inside the admin panle
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'image' ,'description', 'created_at', 'updated_at')
    list_editable = ('description',)
    list_per_page = 5
    search_fields = ('title',)
    list_filter =('author',)
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }

# Register post table on admin site 
admin.site.register(Post,PostAdmin)