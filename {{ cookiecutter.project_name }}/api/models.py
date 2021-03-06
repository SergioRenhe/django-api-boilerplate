from django.db import models


class Example(models.Model):
    """
    This is a sample model.
    """
    field_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)