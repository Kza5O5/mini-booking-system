from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    name = models.CharField(
        max_length=255
    )

    description = models.TextField()

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="items"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def str(self):
        return self.name