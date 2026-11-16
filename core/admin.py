from django.contrib import admin

from .models import FarmInformation, SocialMediaLink


@admin.register(FarmInformation)
class FarmInformationAdmin(admin.ModelAdmin):
    list_display = ['farm_name', 'contact_phone', 'email', 'is_active']
    list_filter = ['is_active']
    search_fields = ['farm_name', 'email', 'physical_location']
    fieldsets = (
        ('Profile', {'fields': ('farm_name', 'tagline', 'logo', 'hero_image', 'is_active')}),
        ('Story', {'fields': ('story', 'mission', 'vision', 'farming_philosophy', 'sustainable_commitment')}),
        ('Contact', {'fields': ('contact_phone', 'whatsapp_number', 'email', 'physical_location', 'operating_hours')}),
        ('Map', {'fields': ('google_maps_embed_url', 'google_maps_directions_url')}),
    )


@admin.register(SocialMediaLink)
class SocialMediaLinkAdmin(admin.ModelAdmin):
    list_display = ['platform', 'name', 'url', 'is_active']
    list_filter = ['platform', 'is_active']
    search_fields = ['platform', 'name', 'url']
