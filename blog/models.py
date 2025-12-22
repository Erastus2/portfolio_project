from django.db import models
from django.core.exceptions import ValidationError


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    excerpt = models.TextField(help_text="Short summary for preview cards")
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


from django.db import models
from django.core.exceptions import ValidationError

class BlogContentBlock(models.Model):
    BLOCK_TYPES = (
        ('text', 'Text'),
        ('image', 'Image'),
    )

    blog = models.ForeignKey(
        'BlogPost',
        on_delete=models.CASCADE,
        related_name='blocks'
    )

    block_type = models.CharField(max_length=10, choices=BLOCK_TYPES)
    text = models.TextField(blank=True)  # optional for image blocks
    image = models.ImageField(
        upload_to='blog/content/',
        blank=True,
        null=True  # optional
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']  # ensures blocks are retrieved in order

    def clean(self):
        """
        Validate blocks conditionally:
        - Text blocks must have text
        - Image blocks must have an image
        """
        if self.block_type == 'text' and not self.text:
            raise ValidationError({'text': 'Text is required for text blocks.'})
        if self.block_type == 'image' and not self.image:
            raise ValidationError({'image': 'Image is required for image blocks.'})

    def __str__(self):
        return f"{self.block_type.capitalize()} block ({self.order}) for '{self.blog.title}'"
