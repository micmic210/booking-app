from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from .models import Post
from .forms import CommentForm


class PostList(generic.ListView):
    """
    Displays a list of published blog posts.
    """
    model = Post
    queryset = Post.objects.filter(status=1)
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    paginate_by = 6

def blog_detail(request, id):
    """
    Displays a single blog post along with its comments and a comment form.
    """
    blog = get_object_or_404(Post, id=id)
    comments = blog.comments.all().order_by("-created_on")
    comment_count = comments.count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = blog
            comment.save()
            messages.success(request, "Your comment has been added successfully.")
            return redirect('blog_detail', id=blog.id)         

    else:
        comment_form = CommentForm()

    return render(
        request,
        'blog/blog_detail.html',
        {
            'blog': blog,
            'comments': comments,
            'comment_count': comment_count,
            'comment_form': comment_form,
        }
    )

