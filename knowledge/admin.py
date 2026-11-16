from django.contrib import admin

from .models import Article, ArticleCategory


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'author', 'published_at']
    list_filter = ['status', 'category']
    search_fields = ['title', 'author', 'excerpt']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-published_at', '-created_at']
    fieldsets = (
        ('Content', {'fields': ('title', 'slug', 'category', 'author', 'featured_image', 'excerpt', 'content')}),
        ('Publishing', {'fields': ('status', 'published_at')}),
    )
