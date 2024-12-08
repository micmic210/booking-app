from django.db import models
from cloudinary.models import CloudinaryField


class Menu(models.Model):
    """
    Model for menu items.
    """
    CATEGORY_CHOICES = [
        ('ramen', 'Ramen'),
        ('starters', 'Starters'),
        ('appetizers', 'Appetizers'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='ramen',
    )
    image = CloudinaryField(
        'image',
        folder="menu_images/",
        use_filename=True,
        unique_filename=False,
    )
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
