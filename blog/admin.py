from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

from .models import Post, Comment, Category # Import all models
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    prepopulated_fields = {'slug':('title',)}
    list_display = ['title', 'slug', 'created_at', 'category']  # Columns to display in the admin list view
    search_fields = ['title']  # Add a search bar for these fields
    list_filter = ('created_at', 'category')  # Add filters for specific fields

# Optional: Customise Comment admin display
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'user', 'created_at']  # Columns to display in the admin list view
    search_fields = ('user', 'body')  # Add a search bar for these fields
    list_filter = ('created_at',)  # Add filters for specific fields

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'slug'] 
    search_fields = ['title']

class Summernote(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
