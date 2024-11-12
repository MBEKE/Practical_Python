from django.shortcuts import render
from .models import BlogPost

# Create your views here.
def homepage(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/homepage.html', {'posts': posts})


# post-detail
def post_detail(requests, post_id):
    post = get_object_or_404(Post, id=post_id) # Retrieve the post by ID, or return 404 if not found
    return render(request, 'blog/post_detail.html', {'post':  post})
