from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created_on')
    list_filter = ('status', 'author', 'created_on')
    search_fields = ('title', 'content')
    ordering = ['-created_on']
