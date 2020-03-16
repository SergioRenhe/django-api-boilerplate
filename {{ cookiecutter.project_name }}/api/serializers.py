from rest_framework import serializers

from .models import Example


class ExampleSerializer(serializers.ModelSerializer):
    """
    This is a sample serializer.
    """
    class Meta:
        model = Example
        exclude = ["id"]
