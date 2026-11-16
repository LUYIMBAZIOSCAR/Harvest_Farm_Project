from django.db import models


class FarmInformation(models.Model):
    farm_name = models.CharField(max_length=200, default='Harvest Farm')
    tagline = models.CharField(max_length=255, blank=True)
    story = models.TextField(blank=True)
    mission = models.TextField(blank=True)
    vision = models.TextField(blank=True)
    farming_philosophy = models.TextField(blank=True)
    sustainable_commitment = models.TextField(blank=True)
    contact_phone = models.CharField(max_length=50, blank=True)
    whatsapp_number = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    physical_location = models.CharField(max_length=255, blank=True)
    google_maps_embed_url = models.URLField(blank=True)
    google_maps_directions_url = models.URLField(blank=True)
    operating_hours = models.CharField(max_length=200, blank=True)
    logo = models.ImageField(upload_to='farm/', blank=True, null=True)
    hero_image = models.ImageField(upload_to='farm/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Farm Information'
        verbose_name_plural = 'Farm Information'
        ordering = ['-created_at']

    def __str__(self):
        return self.farm_name


class SocialMediaLink(models.Model):
    PLATFORM_CHOICES = [
        ('youtube', 'YouTube'),
        ('tiktok', 'TikTok'),
        ('google', 'Google Business Profile'),
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('linkedin', 'LinkedIn'),
    ]

    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    name = models.CharField(max_length=100, blank=True)
    url = models.URLField(help_text='Official profile or page URL')
    icon = models.CharField(max_length=50, default='bi-link-45deg', help_text='Bootstrap icon class')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['platform']

    def __str__(self):
        return self.get_platform_display() or self.name or 'Social Link'
