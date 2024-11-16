from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost 
from .forms import PostForm  

# Homepage view
def homepage(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/homepage.html', {'posts': posts})

# Post detail view
def post_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

# View to add a new post
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to homepage or list of posts
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})

# View to edit an existing post
def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)  # Redirect to post detail view
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})

def delete_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.metthod == "POST":
        post.delete()
        return redirect("homepage")
    return render(request, 'blog/delete_post.html',{'post': post})
