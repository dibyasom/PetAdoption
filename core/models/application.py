from email.policy import default
import imp
from django.db import models

# Import foreign model
from core.models.pet import Pet


class Application(models.Model):
    # Default application time
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    # Foreign Key
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="applications")
    email = models.EmailField(blank=True, null=True, unique=True)
    reason = models.TextField(max_length=500, blank=True, null=True)
    status = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self) -> str:
        return str(self.email)
