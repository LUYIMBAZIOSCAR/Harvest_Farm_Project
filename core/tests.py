from django.test import TestCase

from core.models import FarmInformation


class CoreViewsTests(TestCase):
    def setUp(self):
        FarmInformation.objects.create(
            farm_name='Harvest Farm',
            story='A sustainable farm for learning and production.',
            mission='To educate and build resilient agriculture.',
            is_active=True,
        )

    def test_home_page_loads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Harvest Farm')

    def test_about_page_loads(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'About Harvest Farm')
