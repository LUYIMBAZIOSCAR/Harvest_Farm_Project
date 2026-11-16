from datetime import date

from django import forms

from .models import FarmTourBooking


class FarmTourBookingForm(forms.ModelForm):
    class Meta:
        model = FarmTourBooking
        fields = [
            'full_name',
            'organization',
            'email',
            'telephone',
            'booking_date',
            'preferred_time',
            'number_of_visitors',
            'visit_purpose',
            'areas_of_interest',
            'additional_message',
        ]
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'}),
            'additional_message': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_booking_date(self):
        booking_date = self.cleaned_data.get('booking_date')
        if booking_date and booking_date < date.today():
            raise forms.ValidationError('Please select a future date for your farm visit request.')
        return booking_date
