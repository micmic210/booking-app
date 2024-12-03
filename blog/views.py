from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
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


def comment_edit(request, id, comment_id):
    """
    Edit a specific comment directly on the blog detail page.
    """
    blog = get_object_or_404(Post, id=id)
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.author != request.user:
        messages.error(request, "You are not authorized to edit this comment.")
        return redirect('blog_detail', id=blog.id)

    if request.method == "POST":
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment_form.save()
            messages.success(request, "Your comment has been successfully updated.")
            return redirect('blog_detail', id=blog.id)
        else:
            messages.error(request, "There was an error updating your comment.")
    else:
        comment_form = CommentForm(instance=comment)

    # Pass the edit_comment instance to the template
    return render(
        request,
        'blog/blog_detail.html',
        {
            'blog': blog,
            'comments': blog.comments.all().order_by("-created_on"),
            'comment_form': comment_form,
            'edit_comment': comment,
        }
    )



def comment_delete(request, id, comment_id):
    """
    Delete a specific comment.
    """
    blog = get_object_or_404(Post, id=id)
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.author == request.user:  # Check if the current user is the comment's author
        comment.delete()
        messages.success(request, "Your comment has been successfully deleted.")
    else:
        messages.error(request, "You are not authorized to delete this comment.")
    return redirect('blog_detail', id=blog.id)



