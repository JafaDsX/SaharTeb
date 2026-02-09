from django.contrib.admin import register, ModelAdmin, TabularInline
from blog.models import Blog, BlogSection, Comment, RelatedBlog


class BlogSectionInline(TabularInline):
    model = BlogSection
    extra = 1

class RelatedBlogInline(TabularInline):
    model = TabularInline
    extra = 1


@register(Blog)
class BlogAdmin(ModelAdmin):
    list_display = ("title", 'created_at', 'is_published')
    list_editable = ('is_published',)
    inlines = [BlogSectionInline]


@register(Comment)
class BlogCommentAdmin(ModelAdmin):
    list_display = (
        'blog__title',
        'name', 'email', 'content', 'created_at',
        'is_published'
    )
    list_editable = ('is_published',)
