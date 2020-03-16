from datetime import datetime

from django.urls import reverse
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APITestCase

from .serializers import ExampleSerializer


class TestExample(APITestCase):
    """
    This is a sample test.
    """

    def setUp(self):

        self.example = baker.make(
            "api.Example",
            created_at=datetime.now(),
            updated_at=datetime.now()
        )

        self.list_url = reverse("example-list")
        self.detail_url = reverse(
            "example-detail",
            kwargs={'pk': self.example.id}
        )

    def test_should_list_examples(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_should_retrieve_example(self):
        response = self.client.get(
            self.list_url.format(pk=self.example.id)
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_should_create_example(self):
        example = baker.prepare(
            "api.Example",
            created_at=datetime.now(),
            updated_at=datetime.now()

        )
        serializer = ExampleSerializer(example)
        response = self.client.post(self.list_url, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_should_update_example(self):
        detail_url = reverse(
            "example-detail",
            kwargs={'pk': self.example.id}
        )
        self.example.updated_at = datetime.now()
        serializer = ExampleSerializer(self.example)
        response = self.client.put(self.detail_url, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_should_delete_example(self):
        example = baker.make(
            "api.Example",
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        detail_url = reverse(
            "example-detail",
            kwargs={'pk': example.id}
        )
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
