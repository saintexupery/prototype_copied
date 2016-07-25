from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import CommentForm

def index(request):
    post_list = Post.objects.all()

    return render(request, 'blog/index.html', {
        'post_list' : post_list,
    })

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            return redirect('blog:post_detail', pk)
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post' : post,
        'form' : form,
    })