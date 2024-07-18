from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from events.models import Event
from events.serializers import EventSerializer
from events.views import CreateEvent

# Shortcut for accessing the user model
User = get_user_model()

class TestCreateEventView(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='test_user', password='secret')
        # Create a test client
        self.client = Client()

    def test_create_event_with_form(self):
        # Login the user
        self.client.login(username='test_user', password='secret')

        # Valid form data
        data = {
            'name': 'Test Event',
            'description': 'This is a test event description.',
            'date': '2024-07-20 10:00:00',  # Example datetime format
        }

        # Send a POST request with form data
        response = self.client.post(reverse('create-event'), data=data, content_type='application/x-www-form-urlencoded')

        # Check status code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check response data
        serializer = EventSerializer(Event.objects.get(creator=self.user))
        self.assertEqual(response.data, serializer.data)

    def test_create_event_with_serializer(self):
        # Login the user
        self.client.login(username='test_user', password='secret')

        # Valid JSON data
        data = {
            'name': 'Test Event',
            'description': 'This is a test event description.',
            'date': '2024-07-20 10:00:00',  # Example datetime format
        }

        # Send a POST request with JSON data
        response = self.client.post(reverse('create-event'), json=data, content_type='application/json')

        # Check status code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check response data
        serializer = EventSerializer(Event.objects.get(creator=self.user))
        self.assertEqual(response.data, serializer.data)

    def test_create_event_with_invalid_form_data(self):
        # Login the user
        self.client.login(username='test_user', password='secret')

        # Invalid form data (missing name)
        data = {
            'description': 'This is a test event description.',
            'date': '2024-07-20 10:00:00',
        }

        # Send a POST request with form data
        response = self.client.post(reverse('create-event'), data=data, content_type='application/x-www-form-urlencoded')

        # Check status code
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Check response data contains error message
        self.assertIn('name', response.data)

    def test_create_event_with_unauthorized_user(self):
        # Don't login the user

        # Valid form data
        data = {
            'name': 'Test Event',
            'description': 'This is a test event description.',
            'date': '2024-07-20 10:00:00',
        }

        # Send a POST request with form data
        response = self.client.post(reverse('create-event'), data=data, content_type='application/x-www-form-urlencoded')

        # Check status code
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)  # User not authenticated

class TestEventDetailView(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='test_user', password='secret')
        # Create a test event
        self.event = Event.objects.create(
            name='Test Event',
            description='This is a test event description.',
            date='2024-07-20 10:00:00',
            creator=self.user
        )
        # Create a test client
        self.client.login(username='test_user', password='secret')

    def test_get_event_detail(self):
        # Get the event detail URL
        url = reverse('event-detail', kwargs={'pk': self.event.pk})

        # Send a GET request
        response = self.client.get(url)

        # Check status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check response data
        serializer = EventSerializer(self.event)
        self.assertEqual(response.data, serializer.data)

    def test_get_nonexistent_event(self):
        # Non-existent event ID
        nonexistent_pk = 100  # Replace with a non-existent ID

        # Get the event detail URL
        url = reverse('event-detail', kwargs={'pk': nonexistent_pk})

        # Send a GET request
        response = self.client.get(url)

        # Check status code
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # Check response data
        self.assertEqual(response.data, {'message': 'This event does not exist'})