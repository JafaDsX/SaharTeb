from django.contrib.admin import register, ModelAdmin, TabularInline, StackedInline
from blog.models import Blog, BlogSection, Comment, RelatedBlog, BlogAuthor, BlogTag, BlogCategory


class BlogSectionInline(StackedInline):
    model = BlogSection
    extra = 1

class RelatedBlogInline(TabularInline):
    model = RelatedBlog
    fk_name='blog'
    extra = 1

class BlogTagInline(TabularInline):
    model = BlogTag
    extra = 1


@register(BlogCategory)
class BlogCategoryAdmin(ModelAdmin):
    list_display = ("name", 'slug')


@register(BlogAuthor)
class BlogAuthorAdmin(ModelAdmin):
    list_display = ("name", "bio")


@register(Blog)
class BlogAdmin(ModelAdmin):
    list_display = ("title", 'created_at', 'is_published', 'slug')
    list_editable = ('is_published',)
    inlines = [BlogSectionInline, BlogTagInline, RelatedBlogInline]


@register(Comment)
class BlogCommentAdmin(ModelAdmin):
    list_display = (
        'blog__title',
        'name', 'email', 'content', 'created_at',
        'is_published'
    )
    list_editable = ('is_published',)
