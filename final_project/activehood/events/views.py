from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Event
from .serializers import EventSerializer
from .forms import EventForm
# from rest_framework.filters import GeoDjangoFilter

class CreateEvent(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = EventSerializer
        if serializer.is_valid():
            if 'location' not in request.data:
        # Set a temporary location (replace with your logic later)
                serializer.validated_data['location'] = "Placeholder City"
            serializer.save(creator=request.user)  
            return Response(serializer.data, status=201)  
        return Response(serializer.errors, status=400)  

class EventDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get (self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return Response(status=404)  

        serializer = EventSerializer(event)
        return Response(serializer.data)

class MyEventsList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Event.objects.filter(creator=user)

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(creator=request.user)  
            return Response(serializer.data, status=201)  
        return Response(serializer.errors, status=400) 
    
    serializer_class = EventSerializer


class UserEventsList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        if user_id:
            try:
                user = User.objects.get(pk=user_id)
                return Event.objects.filter(creator=user)
            except User.DoesNotExist:
                return Event.objects.none()
        else:
            return Event.objects.none()

    serializer_class = EventSerializer
    
class EventListByLocation(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    #filter_backends = [filters.GeoDjangoFilter]
    #geo_field = 'location'  # Assuming 'location' field stores geospatial data

    def get_queryset(self):
        user_latitude = self.request.query_params.get('latitude')
        user_longitude = self.request.query_params.get('longitude')
        # Implement logic to filter based on user location (e.g., radius)
        # This is a placeholder, replace with your location filtering logic
        if user_latitude and user_longitude:
            # ... filter based on user coordinates and radius
            return Event.objects.all()  # Replace with filtered queryset
        else:
            return Event.objects.none()  # Return empty queryset if no location provided

    serializer_class = EventSerializer


