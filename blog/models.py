from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    Model for blog posts
    """
    title = models.CharField(max_length=200, unique=True, verbose_name="Title")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts", verbose_name="Author"
    )
    content = models.TextField(verbose_name="Content")
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Created On")
    updated_on = models.DateTimeField(auto_now=True, verbose_name="Updated On")
    status = models.IntegerField(
        choices=STATUS, 
        default=0, 
        verbose_name="Status",
        help_text="0 = Draft, 1 = Published"
    )
    featured_image = CloudinaryField(
        "image",
        folder="blog_images/",
        blank=True,
        null=True,
        verbose_name="Thumbnail Image"
    )
    excerpt = models.TextField(blank=True, verbose_name="Excerpt")

    class Meta:
        ordering = ["-created_on"]
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
    
    def __str__(self):
        return f"{self.title} | written by {self.author}"
