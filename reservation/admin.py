from django.contrib import admin
from .models import Table, Reservation


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Table model.
    """
    list_display = (
        'table_number',
        'capacity',
        'is_available',
        'created_at'
    )
    list_filter = ('is_available',)
    search_fields = ('table_number',)


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Reservation model.
    """
    list_display = (
        'name',
        'reservation_date',
        'reservation_time',
        'guests',
        'status',
        'table',
        'created_at'
    )
    list_filter = ('status', 'reservation_date', 'table')
    search_fields = ('name', 'email', 'phone', 'reservation_number')
    readonly_fields = ('reservation_number',)
