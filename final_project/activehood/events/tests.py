from django.test import TestCase
from django.contrib.auth.models import User

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from events.models import Event
from events.serializers import EventSerializer

class EventDetailTest(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='loui', password='9090909l')

        # Create a test event
        self.event = Event.objects.create(
            name='Test Event',
            description='This is a test event description.',
            date='2024-07-20 10:00:00',
            creator=self.user,
        )

    def test_get_existing_event(self):
        """Test retrieving an existing event detail."""
        url = reverse('events_detail', kwargs={'pk': self.event.pk})
        self.client.force_authenticate(user=self.user)  # Authenticate user
        response = self.client.get(url)

        # Check status code and response data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = EventSerializer(self.event, include='participants')
        self.assertEqual(response.data, serializer.data)

    def test_get_nonexistent_event(self):
        """Test retrieving a non-existent event."""
        url = reverse('events_detail', kwargs={'pk': 1000})  # Non-existent event ID
        self.client.force_authenticate(user=self.user)  # Authenticate user
        response = self.client.get(url)

        # Check status code
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
