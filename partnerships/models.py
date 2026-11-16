from django.db import models


class PartnershipApplication(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('under_review', 'Under Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    PARTNERSHIP_TYPES = [
        ('training_capacity_building', 'Training and Capacity Building'),
        ('research_innovation', 'Research and Innovation'),
        ('agricultural_development', 'Agricultural Development'),
        ('institutional_collaboration', 'Institutional Collaboration'),
        ('sponsorship', 'Sponsorship'),
        ('other', 'Other'),
    ]

    full_name = models.CharField(max_length=150)
    organization_name = models.CharField(max_length=200)
    email = models.EmailField()
    telephone = models.CharField(max_length=50)
    partnership_type = models.CharField(max_length=50, choices=PARTNERSHIP_TYPES)
    subject = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='pending')
    admin_notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.full_name} - {self.organization_name}'
