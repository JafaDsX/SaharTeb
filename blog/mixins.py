from blog.models import BlogCategory
from django.db.models import Count

class BlogCategoryMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_categories'] = BlogCategory.objects.annotate(
            blogs_count=Count("blogs")
        )
        return context

