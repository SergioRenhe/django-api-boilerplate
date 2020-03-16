from rest_framework import viewsets

from .models import Example
from .serializers import ExampleSerializer


class ExampleViewSet(viewsets.ModelViewSet):
    """
    This is a sample view set.
    """
    serializer_class = ExampleSerializer
    queryset = Example.objects.all()