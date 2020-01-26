from django.shortcuts import render, get_object_or_404, redirect
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

def create_or_edit_post(request, pk=None):
    # Create a post or edit an existing post.

    post = get_object_or_404(Post, pk=pk) if pk else None
    if request.method == "POST":
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blogpostform.html', {'form': form})
