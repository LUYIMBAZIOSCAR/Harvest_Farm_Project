from django.test import TestCase

from contact.models import ContactMessage


class ContactTests(TestCase):
    def test_contact_form_submission_stores_message(self):
        response = self.client.post('/contact/', {
            'full_name': 'Asha Visitor',
            'email': 'asha@example.com',
            'telephone': '+256700000004',
            'subject': 'General enquiry',
            'message': 'We would like to learn more about your farm.',
        })
        self.assertEqual(response.status_code, 302)
        message = ContactMessage.objects.get(email='asha@example.com')
        self.assertEqual(message.subject, 'General enquiry')

    def test_contact_page_loads(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Contact Us')
