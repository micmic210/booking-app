from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment, Category
from .forms import CommentForm
from django.http import JsonResponse



class PostList(generic.ListView):
    """
    Displays a list of published blog posts, with optional category filtering.
    - Retrieves all posts with status=1 (Published).
    - Paginated by 6 posts per page.
    """
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        """
        Returns the queryset of posts, optionally filtered by category.
        """
        category_id = self.request.GET.get('category')
        if category_id:
            return Post.objects.filter(categories__id=category_id, status=1)
        return Post.objects.filter(status=1)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()  
        return context


def blog_detail(request, id):
    """
    Displays a single blog post along with its comments and a comment form.
    - Handles comment submission if the request method is POST.
    - Returns the blog post, comments, and the comment form for the template.
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


def like_post(request, id):
    """
    Handles the like/unlike functionality for a blog post.
    """
    post = get_object_or_404(Post, id=id)

    if request.user.is_authenticated:
        if request.user in post.likes.all():
            post.likes.remove(request.user)
            liked = False
        else:
            post.likes.add(request.user)
            liked = True

        return JsonResponse({
            'liked': liked,
            'likes_count': post.likes.count(),
        })
    else:
        return JsonResponse({'error': 'You must be logged in to like posts.'}, status=401)
