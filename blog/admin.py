from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import BlogPost, BlogContentBlock


class BlogContentBlockInline(admin.TabularInline):
    model = BlogContentBlock
    extra = 1


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "published", "created_at")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [BlogContentBlockInline]
