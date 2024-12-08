from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Admin configuration for blog posts.
    """
    list_display = ('title', 'author', 'status', 'created_on')
    list_filter = ('status', 'author', 'created_on')
    search_fields = ('title', 'content')
    ordering = ['-created_on']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin configuration for comments.
    """
    list_display = ('author', 'post', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('author__username', 'body')
