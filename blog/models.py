from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.db.models import Q
import unicodedata, os

class BlogCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name="نام دسته بندی")
    slug = models.SlugField(unique=True, verbose_name="اسلاگ", blank=True, allow_unicode=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name='دسته بندی'
        verbose_name_plural='دسته بندی ها'


class BlogAuthor(models.Model):
    name = models.CharField(max_length=255, verbose_name="نام نویسنده")
    bio = models.TextField(blank=True, null=True, verbose_name="بیوگرافی نویسنده")
    profile_picture = models.ImageField(upload_to='author_profiles/', blank=True, null=True, verbose_name="عکس پروفایل نویسنده")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='نویسنده'
        verbose_name_plural='نویسندگان'



class BlogQuerySet(models.QuerySet):

    def published(self):
        return self.filter(is_published=True)

    def category(self, category_slug):
        return self.filter(category__slug=category_slug)

    def search(self, query):
        if not query:
            return self

        return self.filter(
            Q(title__icontains=query) |
            Q(introduction__icontains=query) |
            Q(sections__text__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()

def safe_upload_to(instance, filename):
    base, ext = os.path.splitext(filename)
    base_normalized = unicodedata.normalize('NFKD', base).encode('ascii', 'ignore').decode('ascii')
    safe_name = base_normalized.replace(' ', '_')
    return f"images/{safe_name}{ext}"

class Blog(models.Model):
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='blogs', verbose_name="دسته بندی")
    title = models.CharField(max_length=255, verbose_name="عنوان")
    slug = models.SlugField(unique=True, verbose_name="اسلاگ", null=True, blank=True, allow_unicode=True, max_length=255)
    introduction = models.CharField(max_length=255, blank=True, verbose_name='مقدمه')
    author = models.ForeignKey(BlogAuthor, on_delete=models.SET_NULL, null=True, blank=True, related_name='blogs', verbose_name="نویسنده")
    is_published = models.BooleanField(default=False, verbose_name="منتشر شده")
    time_to_read = models.PositiveIntegerField(null=True, blank=True, verbose_name="زمان تقریبی مطالعه (دقیقه)", default=5)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")


    img = models.ImageField(upload_to=safe_upload_to)

    objects = BlogQuerySet.as_manager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.title.replace(' ', '-')
        super().save(*args, **kwargs)

    @property
    def main_tag(self):
        return self.tags.filter(is_main=True).first()

    class Meta:
        verbose_name='وبلاگ'
        verbose_name_plural='وبلاگ ها'

    def __str__(self):
        return self.title





class BlogSection(models.Model):

    TYPE_CHOICES = [
        ('text', 'Text'),
        ('image', 'Image'),
    ]

    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="عنوان بخش")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='sections', verbose_name="مقاله")
    text = RichTextField(blank=True, null=True, verbose_name="متن بخش")
    blockquote = models.TextField( null=True, blank=True, verbose_name='مطلب مهم')
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True, verbose_name="تصویر بخش")
    is_main = models.BooleanField(default=False, verbose_name="بخش اصلی")

    def __str__(self):
        return f"{self.blog.title}"

    class Meta:
        verbose_name='بخش وبلاگ'
        verbose_name_plural='بخش های وبلاگ'



class RelatedBlog(models.Model):
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='related_blogs',
        verbose_name="مقاله اصلی"
    )
    related_blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='related_to',
        verbose_name="مقاله مرتبط"
    )

    class Meta:
        verbose_name = 'مقاله مرتبط'
        verbose_name_plural = 'مقالات مرتبط'
        unique_together = ('blog', 'related_blog')


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments', verbose_name="مقاله")
    name = models.CharField(max_length=255, verbose_name="نام")
    email = models.EmailField(verbose_name="ایمیل")
    content = models.TextField(verbose_name="متن نظر")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    is_published = models.BooleanField(default=False, verbose_name="منتشر شده")

    def __str__(self):
        return f"Comment by {self.name} on {self.blog.title}"

    class Meta:
        verbose_name='نظرات'
        verbose_name_plural='نظرات'


class BlogTag(models.Model):
    blog = models.ForeignKey(Blog, related_name='tags', on_delete=models.CASCADE, verbose_name="مقالات مرتبط")
    name = models.CharField(max_length=50, unique=True, verbose_name="نام تگ")
    is_main = models.BooleanField(default=False, verbose_name="تگ اصلی")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='تگ'
        verbose_name_plural='تگ ها'


