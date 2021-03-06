from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm

# Create your views here.
def get_posts(request):
    # This will return all posts from the database.
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    return render(request, "blogpost.html", {'posts': posts})

def post_detail(request, pk):
    # Returns a single post base on the post ID(pk)
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, "postdetail.html", {'post': post})

@login_required()
def create_or_edit_post(request, pk=None):
    # Create a post or edit an existing post.
    if request.user.is_superuser:
        post = get_object_or_404(Post, pk=pk) if pk else None
        if request.method == "POST":
            form = BlogPostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save()
                messages.success(request, "Edit/create was successfull!")
                
                return redirect(post_detail, post.pk)
        else:
            form = BlogPostForm(instance=post)
        return render(request, 'blogpostform.html', {'form': form})
    else:
        return redirect(get_posts)

@login_required()
def delete_post(request, pk):
    # Delete an existingg post
    if request.user.is_superuser:
        post = get_object_or_404(Post, pk=pk)
        post.delete()

        return redirect(get_posts)

    else:
        return redirect(get_posts)