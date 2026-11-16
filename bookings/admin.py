from django.contrib import admin

from .models import FarmTourBooking


@admin.register(FarmTourBooking)
class FarmTourBookingAdmin(admin.ModelAdmin):
    list_display = ['booking_reference', 'full_name', 'booking_date', 'status', 'number_of_visitors']
    list_filter = ['status', 'visit_purpose']
    search_fields = ['booking_reference', 'full_name', 'email', 'organization']
    ordering = ['-created_at']
    readonly_fields = ['booking_reference', 'created_at', 'updated_at']
    fieldsets = (
        ('Visitor Details', {'fields': ('full_name', 'organization', 'email', 'telephone')}),
        ('Visit Details', {'fields': ('booking_date', 'preferred_time', 'number_of_visitors', 'visit_purpose', 'areas_of_interest', 'additional_message')}),
        ('Administration', {'fields': ('status', 'admin_notes', 'booking_reference', 'created_at', 'updated_at')}),
    )
