from django import forms
from .models import Post

# Newsitem form
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'content')