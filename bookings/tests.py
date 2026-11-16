from django.test import TestCase

from bookings.models import FarmTourBooking


class FarmTourBookingTests(TestCase):
    def test_booking_submission_creates_pending_record(self):
        response = self.client.post('/book-tour/', {
            'full_name': 'Test Visitor',
            'organization': 'Farm Learning Centre',
            'email': 'visitor@example.com',
            'telephone': '+256700000001',
            'booking_date': '2099-01-12',
            'preferred_time': '10:00',
            'number_of_visitors': 5,
            'visit_purpose': 'educational_visit',
            'areas_of_interest': 'poultry',
            'additional_message': 'We want to learn about poultry management.',
        })
        self.assertEqual(response.status_code, 302)
        booking = FarmTourBooking.objects.get(email='visitor@example.com')
        self.assertEqual(booking.status, 'pending')
        self.assertTrue(booking.booking_reference)

    def test_past_booking_date_is_rejected(self):
        response = self.client.post('/book-tour/', {
            'full_name': 'Old Visitor',
            'organization': 'Old School',
            'email': 'old@example.com',
            'telephone': '+256700000002',
            'booking_date': '2020-01-12',
            'preferred_time': '11:00',
            'number_of_visitors': 2,
            'visit_purpose': 'general_farm_tour',
            'areas_of_interest': 'dairy_farming',
            'additional_message': 'Old date',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please select a future date')
