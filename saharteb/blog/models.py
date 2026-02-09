from django.db import models




class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    slug = models.SlugField(unique=True, verbose_name="اسلاگ", null=True, blank=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.title.replace(" ", "-").lower()
        super().save(*args, **kwargs)

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
    text = models.TextField(blank=True, null=True, verbose_name="متن بخش")
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True, verbose_name="تصویر بخش")


    def __str__(self):
        return f"{self.blog.title}"


class RelatedBlog(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='related_blogs', verbose_name="مقاله اصلی")
    related_blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='related_to_blogs', verbose_name="مقاله مرتبط")

    def __str__(self):
        return f"{self.blog.title} is related to {self.related_blog.title}"


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
