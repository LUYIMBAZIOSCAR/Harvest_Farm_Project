from django.db import models
from django.utils.text import slugify


class GalleryCategory(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name = 'Gallery Category'
        verbose_name_plural = 'Gallery Categories'
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class GalleryItem(models.Model):
    title = models.CharField(max_length=180)
    category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE, related_name='items')
    image = models.ImageField(upload_to='gallery/', blank=True, null=True)
    video_url = models.URLField(blank=True, help_text='YouTube or other video URL')
    description = models.TextField(blank=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-is_featured', '-created_at']

    def __str__(self):
        return self.title

    @property
    def has_media(self):
        return bool(self.image or self.video_url)

    def get_embed_url(self):
        if not self.video_url:
            return ''
        if 'youtube.com/watch?v=' in self.video_url:
            video_id = self.video_url.split('v=')[1].split('&')[0]
            return f'https://www.youtube.com/embed/{video_id}'
        if 'youtu.be/' in self.video_url:
            video_id = self.video_url.split('youtu.be/')[-1].split('?')[0]
            return f'https://www.youtube.com/embed/{video_id}'
        return self.video_url
