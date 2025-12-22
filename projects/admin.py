from django.contrib import admin
from .models import Project
# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "is_featured", "created_at")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("is_featured", "created_at")
    search_fields = ("title", "description")

