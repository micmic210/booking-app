from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm


class PostList(generic.ListView):
    """
    Displays a list of published blog posts.
    - Retrieves all posts with status=1 (Published).
    - Paginated by 6 posts per page.
    """
    model = Post
    queryset = Post.objects.filter(status=1)
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    paginate_by = 6


def blog_detail(request, id):
    """
    Displays a single blog post along with its comments and a comment form.
    - Handles comment submission if the request method is POST.
    - Returns the blog post, comments, and the comment form for the template.

    Args:
    - request: The HTTP request object.
    - id: The ID of the blog post.

    Returns:
    - Renders 'blog/blog_detail.html' with the post, comments, and comment form.
    """
    # Get the blog post by ID or return a 404 error if not found
    blog = get_object_or_404(Post, id=id)
    
    # Retrieve all comments related to the blog post
    comments = blog.comments.all().order_by("-created_on")
    comment_count = comments.count()

    if request.method == "POST":
        # Handle new comment submission
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user  # Set the current user as the comment author
            comment.post = blog  # Link the comment to the blog post
            comment.save()
            messages.success(request, "Your comment has been added successfully.") 
            return redirect('blog_detail', id=blog.id)
    else:
        # Initialize an empty comment form for GET requests
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
    - Ensures that only the author of the comment can edit it.
    - Returns the edited comment form or updates the comment on POST.

    Args:
    - request: The HTTP request object.
    - id: The ID of the blog post.
    - comment_id: The ID of the comment to edit.

    Returns:
    - Renders 'blog/blog_detail.html' with the edit form or redirects after editing.
    """
    # Get the blog post and comment by their IDs or return a 404 error
    blog = get_object_or_404(Post, id=id)
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.author != request.user:
        # Prevent unauthorized users from editing comments
        messages.error(request, "You are not authorized to edit this comment.")
        return redirect('blog_detail', id=blog.id)

    if request.method == "POST":
        # Update the comment with the submitted data
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment_form.save()
            messages.success(request, "Your comment has been successfully updated.")
            return redirect('blog_detail', id=blog.id)
        else:
            messages.error(request, "There was an error updating your comment.")
    else:
        # Pre-fill the form with the existing comment data for GET requests
        comment_form = CommentForm(instance=comment)

    return render(
        request,
        'blog/blog_detail.html',
        {
            'blog': blog,
            'comments': blog.comments.all().order_by("-created_on"),
            'comment_form': comment_form,
            'edit_comment': comment,  # Pass the comment being edited to the template
        }
    )


def comment_delete(request, id, comment_id):
    """
    Delete a specific comment.
    - Ensures that only the author of the comment can delete it.
    - Deletes the comment on POST and redirects to the blog detail page.

    Args:
    - request: The HTTP request object.
    - id: The ID of the blog post.
    - comment_id: The ID of the comment to delete.

    Returns:
    - Redirects to the blog detail page after deletion.
    """
    # Get the blog post and comment by their IDs or return a 404 error
    blog = get_object_or_404(Post, id=id)
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.author == request.user:  # Ensure only the comment author can delete it
        comment.delete()
        messages.success(request, "Your comment has been successfully deleted.")
    else:
        # Prevent unauthorized users from deleting comments
        messages.error(request, "You are not authorized to delete this comment.")
    
    return redirect('blog_detail', id=blog.id)

