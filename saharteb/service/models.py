from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=150, unique=True, verbose_name='عنوان دسته بندی')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')

    class Meta:
        verbose_name='دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title



class Service(models.Model):
    SERVICE_TYPES = (
        (1, 'TRANSLATOR'),
        (2, 'DOCTOR'),
        (3, 'HOTEL'),
        (4, 'TREATMENT')
    )

    name = models.CharField(max_length=100, verbose_name='نام سرویس')
    title = models.CharField(max_length=255, null=True, blank=True, verbose_name='عنوان سرویس')
    service_type = models.PositiveSmallIntegerField(choices=SERVICE_TYPES, default=1, verbose_name='نوع سرویس')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='services', verbose_name='دسته بندی')
    is_active = models.BooleanField(default=False, verbose_name='فعال بودن سرویس')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ ایجاد')

    def __str__(self):
        return f"{self.category} - {self.get_service_type_display()}"

    class Meta:
        verbose_name='سرویس'
        verbose_name_plural='سرویس ها'



class ServiceProvider(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='providers', verbose_name='کاربر')
    service = models.ForeignKey(Service, on_delete=models.PROTECT, related_name='providers', verbose_name='سرویس')
    is_active = models.BooleanField(default=False, verbose_name='فعال بودن')


    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')

    def __str__(self):
        return f'{self.user} - {self.service} - {self.is_active}'

    class Meta:
        verbose_name='فراهم کننده سرویس'
        verbose_name_plural='فراهم کنندگان سرویس'



class ServiceProviderOption(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='options', verbose_name='سرویس')
    service_provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE, related_name='options', verbose_name='فراهم کننده سرویس')
    key = models.CharField(max_length=100, verbose_name='کلید گزینه')
    value = models.CharField(max_length=100, verbose_name='مقدار گزینه')

    def __str__(self):
        return f'{self.service} - {self.service_provider}'

    class Meta:
        verbose_name='گزینه فراهم کننده سرویس'
        verbose_name_plural='گزینه های فراهم کنندگان سرویس'


