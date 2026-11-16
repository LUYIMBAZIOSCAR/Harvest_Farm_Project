from django import forms

from .models import PartnershipApplication


class PartnershipApplicationForm(forms.ModelForm):
    class Meta:
        model = PartnershipApplication
        fields = [
            'full_name',
            'organization_name',
            'email',
            'telephone',
            'partnership_type',
            'subject',
            'description',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }
