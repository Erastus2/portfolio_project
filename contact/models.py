from django.db import models
# Create your models here.
# contact/models.py

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # automatically stores submission time

    def __str__(self):
        return f"{self.name} - {self.email}"
