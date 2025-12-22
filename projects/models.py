from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    # Optional image (project thumbnail)
    image = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True
    )

    # Links
    github_url = models.URLField(
        blank=True,
        null=True
    )
    live_url = models.URLField(
        blank=True,
        null=True
    )

    # Skills / Tech stack (linked to skills app)
    tech_stack = models.ManyToManyField(
        "skills.TechItem",
        related_name="projects",
        blank=True
    )

    # Metadata
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
