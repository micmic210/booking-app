from django.db import models
import random
import string

# Table Model
class Table(models.Model):
    table_number = models.PositiveIntegerField(unique=True, null=False)
    capacity = models.PositiveIntegerField(null=False)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Table {self.table_number} (Capacity: {self.capacity})"

    @staticmethod
    def get_default_table():
        """
        Returns the default table object, creating it if it doesn't exist.
        """
        default_table, created = Table.objects.get_or_create(
            table_number=1,
            defaults={
                'capacity': 4,
                'is_available': True,
            }
        )
        return default_table.id


# Reservation Model
class Reservation(models.Model):
    STATUS_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
        ('pending', 'Pending'),
    ]

    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, null=False, blank=False)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name="reservations", default=Table.get_default_table)
    reservation_date = models.DateField(null=False)
    reservation_time = models.TimeField(null=False)
    guests = models.PositiveIntegerField(null=False)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='confirmed')
    created_at = models.DateTimeField(auto_now_add=True)
    reservation_number = models.CharField(max_length=10, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.reservation_number:
            self.reservation_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Reservation {self.id} by {self.name} on {self.reservation_date} at {self.reservation_time}"
