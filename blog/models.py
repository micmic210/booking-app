from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    Model for blog posts
    """
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField(
        folder="blog_images/",
        use_filename=True,
        unique_filename=False,
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    categories = models.ManyToManyField('Category', related_name="posts", blank=True)

    class Meta:
        ordering = ["-created_on"]
    
    def __str__(self):
        return f"{self.title} | written by {self.author}"
    
    def likes_count(self):
        """
        Returns the total number of likes for the post.
        """
        return self.likes.count()


class Comment(models.Model):
    """
    Model for comments on blog posts
    """

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]
        
    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"



class Category(models.Model):
    """
    Model for categories on blog posts
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories" 

    def __str__(self):
        return self.name
