from django.test import TestCase

from knowledge.models import Article, ArticleCategory


class KnowledgeTests(TestCase):
    def setUp(self):
        self.category = ArticleCategory.objects.create(name='Organic Farming', slug='organic-farming')
        self.draft = Article.objects.create(
            title='Draft Article',
            slug='draft-article',
            excerpt='Draft piece',
            content='Draft content',
            category=self.category,
            status='draft',
            author='Farm Team',
        )
        self.published = Article.objects.create(
            title='Published Article',
            slug='published-article',
            excerpt='Published piece',
            content='Published content',
            category=self.category,
            status='published',
            author='Farm Team',
        )

    def test_published_articles_are_publicly_visible(self):
        response = self.client.get('/knowledge/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Published Article')
        self.assertNotContains(response, 'Draft Article')

    def test_article_detail_loads(self):
        response = self.client.get(f'/knowledge/{self.published.slug}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Published Article')
