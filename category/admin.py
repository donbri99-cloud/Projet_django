from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "is_active", "created_at")
    search_fields = ("name",)
    list_filter = ("is_active",)
    readonly_fields = ("slug", "created_at", "updated_at")