from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from events.models import Event
from events.serializers import EventSerializer
from events.forms import EventForm
from django.contrib import messages

# from rest_framework.filters import GeoDjangoFilter

class CreateEvent(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.content_type == 'application/x-www-form-urlencoded':
            form = EventForm(request.POST)
            if form.is_valid():
                event = form.save(commit=False)
                event.creator = request.user
                event.save()
                serializer = EventSerializer(event)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
            
        else: 
            serializer = EventSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(creator=request.user)  
                return Response(serializer.data, status=201)  
            return Response(serializer.errors, status=400) 

class EventDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get (self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return Response({"message": "This event does not exist"}, status=404)  

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


class JoinEvent(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return Response({"message": "This event does not exist"},status=404)

        user = request.user

        # Check if user is already participating
        if user in event.participants.all():
            return Response({"message": "You are already joined to this event"}, status=400)

        event.participants.add(user)
        event.save()
        event = Event.objects.get(pk=event.pk)  # Get the updated event from the database

        serializer = EventSerializer(event)  # Optional for user data
        return Response(serializer.data, status=201)

class LeaveEvent(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return Response({"message": "This event does not exist"}, status=404)

        user = request.user

        # Check if user is participating
        if user not in event.participants.all():
            return Response({"message": "You are not currently joined to this event"}, status=400)

        event.participants.remove(user)
        event.save()

        return Response({"message": "You successfully left this event"},status=204) 

class UpdateEvent(APIView):
    def put(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return Response(status=404)

        # Check if user is authorized to update (creator)
        if event.creator != request.user:
            return Response({"message": "Only the creator can update event"}, status=403)

        serializer = EventSerializer(event, data=request.data, partial=True) # allows updating specific fields without requiring all data.
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def post(self, request, pk):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(creator=request.user)  
            return Response(serializer.data, status=201)  
        return Response(serializer.errors, status=400) 

class DeleteEvent(APIView):
    def delete(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return Response(status=404)

        # Check if user is authorized to delete (creator)
        if event.creator != request.user:
            return Response({"message": "Only the creator can delete event"}, status=403)

        event.delete()
        return Response(status=204)     

    def post(self, request, pk):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(creator=request.user)  
            return Response(serializer.data, status=201)  
        return Response(serializer.errors, status=400) 