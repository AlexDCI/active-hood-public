from rest_framework import serializers
from events.models import Event, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  

class EventSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)  # Nested serializer for participants

    class Meta:
        model = Event
        fields = '__all__' 