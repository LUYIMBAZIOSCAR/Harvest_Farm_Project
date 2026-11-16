from django.test import TestCase

from partnerships.models import PartnershipApplication


class PartnershipApplicationTests(TestCase):
    def test_partnership_submission_saves_application(self):
        response = self.client.post('/partnerships/', {
            'full_name': 'Jane Partner',
            'organization_name': 'Agri Education Network',
            'email': 'jane@example.com',
            'telephone': '+256700000003',
            'partnership_type': 'training_capacity_building',
            'subject': 'Capacity Building Support',
            'description': 'We want to collaborate on practical farmer training sessions.',
        })
        self.assertEqual(response.status_code, 302)
        application = PartnershipApplication.objects.get(email='jane@example.com')
        self.assertEqual(application.status, 'pending')

    def test_partnership_page_loads(self):
        response = self.client.get('/partnerships/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Partnerships')
