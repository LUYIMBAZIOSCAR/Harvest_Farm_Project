from django.db import models


class ContactMessage(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    telephone = models.CharField(max_length=50, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.full_name}: {self.subject}'
