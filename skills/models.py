from django.db import models

# Create your models here.
class TechGroup(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name

# sub Category
class TechCategory(models.Model):
    group = models.ForeignKey(
        TechGroup,
        on_delete=models.CASCADE,
        related_name="categories"
    )

    name = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ["group", "slug"]
        ordering = ["order", "name"]

    def __str__(self):
        return f"{self.group.name} → {self.name}"

# tech Item
class TechItem(models.Model):
    PROFICIENCY_LEVELS = [
        ("basic", "Basic"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
    ]

    category = models.ForeignKey(
        TechCategory,
        on_delete=models.CASCADE,
        related_name="items"
    )

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    proficiency = models.CharField(
        max_length=20,
        choices=PROFICIENCY_LEVELS,
        default="intermediate"
    )

    is_core = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["category", "name"]
        ordering = ["name"]

    def __str__(self):
        return self.name
