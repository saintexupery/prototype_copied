from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from .models import Post, Comment
from .forms import CommentForm

@login_required
def index(request):
    post_list = Post.objects.all()

    return render(request, 'blog/index.html', {
        'post_list' : post_list,
    })

@login_required
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = get_object_or_404(Post, pk=pk)
            comment.user = request.user
            comment.save()
            return redirect('blog:post_detail', pk)
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post' : post,
        'form' : form,
    })