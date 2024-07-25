# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import EventForm
from .models import Event
from django.contrib import messages
from users.models import Activity
from locations.models import City


@login_required
def events_list(request):
    user = request.user
    # location = user.profile.city  # Default to user's city

    # Get location and activity filters from query parameters
    location_param = request.GET.get('location', None)
    activity_param = request.GET.get('activity', None)
    print(request.GET)
    print(activity_param)
    queryset = Event.objects.all()

    # if location:
    #     queryset = queryset.filter(location=location)

    if location_param:
        queryset = queryset.filter(location__name__icontains=location_param)
    
    if activity_param:
        queryset = queryset.filter(activity__name__icontains=activity_param)

    activities = Activity.objects.all()
    locations = City.objects.all()
    events = queryset
    print(events)

    return render(request, 'events_list.html', {
        'events': queryset,
        'activities': activities,
        'locations': locations,
    })


@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.creator = request.user
            event.save()
            messages.success(request, 'Event created successfully.')
            return redirect('events_home')
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})


@login_required
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    user_is_creator = event.creator == request.user
    user_is_participant = request.user in event.participants.all()
    context = {
        'event': event,
        'user_is_creator': user_is_creator,
        'user_is_participant': user_is_participant,
    }

    return render(request, 'event_detail.html', context)


@login_required
def my_events(request):
    events = Event.objects.filter(creator=request.user)
    return render(request, 'my_events.html', {'events': events})


@login_required
def participating(request):
    events = request.user.participating_events.all()
    return render(request, 'participating.html', {'events': events})


@login_required
def user_events(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    events = Event.objects.filter(creator=user)
    return render(request, 'user_events.html', {'events': events})


@login_required
def join_event(request, pk):
    event = get_object_or_404(Event, pk=pk)

    if request.user == event.creator:
        messages.error(request, "You are the owner of this event and cannot join it.")
    elif request.user in event.participants.all():
        messages.error(request, "You are already joined to this event.")
    else:
        event.participants.add(request.user)
        messages.success(request, "You successfully joined the event.")
    
    return redirect('event_detail', pk=pk)

@login_required
def leave_event(request, pk):
    event = get_object_or_404(Event, pk=pk)

    if request.user == event.creator:
        messages.error(request, "You are the owner of this event and cannot leave it.")
    elif request.user not in event.participants.all():
        messages.error(request, "You are not currently joined to this event.")
    else:
        event.participants.remove(request.user)
        messages.success(request, "You successfully left the event.")
    
    return redirect('event_detail', pk=pk)

