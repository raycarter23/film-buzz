from django import forms
from .models import Comment, Post
from django_ckeditor_5.widgets import CKEditor5Widget

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'image')
        widgets = {
            "content": CKEditor5Widget(config_name="extends")
        }
    