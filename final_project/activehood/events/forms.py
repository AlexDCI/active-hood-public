from django import forms
from events.models import Event
from users.models import Activity
from locations.models import City


class EventForm(forms.ModelForm):
    activity = forms.ModelChoiceField(queryset=Activity.objects.all(), empty_label="Select an activity")
    location = forms.ModelChoiceField(queryset=City.objects.all(), empty_label="Select a location")

    class Meta:
        model = Event
        fields = ['activity', 'description', 'date', 'time', 'location']