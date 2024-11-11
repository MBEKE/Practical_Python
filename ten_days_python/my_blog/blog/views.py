from django.shortcuts import render
from .models import BlogPost

# Create your views here.
def homepage(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/homepage.html', {'posts': posts})
