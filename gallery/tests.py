from django.test import TestCase

from gallery.models import GalleryCategory, GalleryItem


class GalleryTests(TestCase):
    def setUp(self):
        self.category = GalleryCategory.objects.create(name='Farm Activities', slug='farm-activities')

    def test_gallery_item_creation(self):
        item = GalleryItem.objects.create(
            title='Farm Training Session',
            category=self.category,
            description='A demonstration session in the field.',
            is_featured=True,
        )
        self.assertTrue(GalleryItem.objects.filter(pk=item.pk).exists())

    def test_gallery_page_loads(self):
        response = self.client.get('/gallery/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Gallery')
