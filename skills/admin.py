from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import TechGroup, TechCategory, TechItem


@admin.register(TechGroup)
class TechGroupAdmin(admin.ModelAdmin):
    list_display = ("name", "order")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("order", "name")


@admin.register(TechCategory)
class TechCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "group", "order")
    list_filter = ("group",)
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("group", "order", "name")


@admin.register(TechItem)
class TechItemAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "get_group",
        "proficiency",
        "is_core",
    )
    list_filter = (
        "category__group",
        "category",
        "proficiency",
        "is_core",
    )
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("category", "name")

    def get_group(self, obj):
        return obj.category.group.name

    get_group.short_description = "Group"
