import uuid
from datetime import date

from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class FarmTourBooking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]

    VISIT_PURPOSE_CHOICES = [
        ('farmer_training', 'Farmer Training'),
        ('educational_visit', 'Educational Visit'),
        ('research', 'Research'),
        ('institutional_visit', 'Institutional Visit'),
        ('general_farm_tour', 'General Farm Tour'),
        ('other', 'Other'),
    ]

    AREAS_OF_INTEREST_CHOICES = [
        ('poultry', 'Poultry'),
        ('goat_farming', 'Goat Farming'),
        ('dairy_farming', 'Dairy Farming'),
        ('banana_production', 'Banana Production'),
        ('organic_farming', 'Organic Farming'),
        ('general_farm_management', 'General Farm Management'),
    ]

    booking_reference = models.CharField(max_length=20, unique=True, blank=True)
    full_name = models.CharField(max_length=150)
    organization = models.CharField(max_length=200, blank=True)
    email = models.EmailField()
    telephone = models.CharField(max_length=50)
    booking_date = models.DateField()
    preferred_time = models.CharField(max_length=50)
    number_of_visitors = models.PositiveIntegerField(default=1)
    visit_purpose = models.CharField(max_length=50, choices=VISIT_PURPOSE_CHOICES)
    areas_of_interest = models.CharField(max_length=100, choices=AREAS_OF_INTEREST_CHOICES)
    additional_message = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    admin_notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def clean(self):
        if self.booking_date and self.booking_date < date.today():
            raise ValidationError({'booking_date': 'Booking date cannot be in the past.'})

    def save(self, *args, **kwargs):
        if not self.booking_reference:
            self.booking_reference = 'HF-' + uuid.uuid4().hex[:8].upper()
        if self.booking_date and self.booking_date < date.today():
            raise ValidationError('Booking date cannot be in the past.')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.full_name} - {self.booking_reference}'
