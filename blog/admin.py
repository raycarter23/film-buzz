from django.contrib import admin

# Register your models here.

from .models import Post, Comment # Import both models
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ['title', 'slug', 'created_at']  # Columns to display in the admin list view
    search_fields = ['title']  # Add a search bar for these fields
    list_filter = ('created_at',)  # Add filters for specific fields

# Optional: Customise Comment admin display
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'user', 'created_at']  # Columns to display in the admin list view
    search_fields = ('user', 'body')  # Add a search bar for these fields
    list_filter = ('created_at',)  # Add filters for specific fields

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
