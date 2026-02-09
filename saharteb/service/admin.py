from django.contrib import admin
from service.models import Category, Service, ServiceProvider, ServiceProviderOption
from django.contrib.admin import register, TabularInline, ModelAdmin


class ServiceProviderOptionInline(TabularInline):
    model = ServiceProviderOption
    extra = 1


@register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    ordering = ('-created_at',)

@register(Service)
class ServiceAdmin(ModelAdmin):
    list_display = ('name', 'title', 'service_type', 'category', 'is_active', 'created_at', 'updated_at')
    list_filter = ('service_type', 'category', 'is_active')
    search_fields = ('name', 'title')
    ordering = ('-created_at',)
    inlines = [ServiceProviderOptionInline]


@register(ServiceProvider)
class ServiceProviderAdmin(ModelAdmin):
    list_display = ('user', 'service', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active',)
    search_fields = ('user__username', 'service__name')
    ordering = ('-created_at',)


