from rest_framework import serializers
from events.models import Event, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  

class EventSerializer(serializers.ModelSerializer):
    participants = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all()) # Nested serializer for participants

    class Meta:
        model = Event
        fields = '__all__' 