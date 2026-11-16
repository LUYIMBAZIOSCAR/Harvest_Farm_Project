from django.contrib import admin

from .models import PartnershipApplication


@admin.register(PartnershipApplication)
class PartnershipApplicationAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'organization_name', 'partnership_type', 'status', 'created_at']
    list_filter = ['status', 'partnership_type']
    search_fields = ['full_name', 'organization_name', 'email', 'subject']
    ordering = ['-created_at']
    fieldsets = (
        ('Applicant Details', {'fields': ('full_name', 'organization_name', 'email', 'telephone')}),
        ('Partnership Request', {'fields': ('partnership_type', 'subject', 'description')}),
        ('Administration', {'fields': ('status', 'admin_notes')}),
    )
