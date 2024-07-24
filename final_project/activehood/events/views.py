from django.shortcuts import render, redirect
import requests
from django.http import HttpResponse
from events.forms import EventForm


def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            api_url = 'http://127.0.0.1:8000/api/create/'
            event_data = form.cleaned_data
            try:
                response = requests.post(api_url, json=event_data)
                response.raise_for_status()
                return redirect('events_home')  
            except requests.exceptions.RequestException as e:
                return HttpResponse(f"An error occurred: {e}", status=500)
    else:
        form = EventForm()
    
    return render(request, 'create_event.html', {'form': form})


def event_detail(request, pk):
    api_url = f'http://127.0.0.1:8000/events/api/{pk}/'
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        context = {'event': data}
    except requests.exceptions.RequestException as e:
        return HttpResponse(f"An error occurred: {e}", status=500)
    
    return render(request, 'event_detail.html', context)


def join_event(request, pk):
    api_url = f'http://127.0.0.1:8000/events/api/join/{pk}/'
    headers = {'Authorization': f'Bearer {request.session["auth_token"]}'}

    try:
        response = requests.post(api_url, headers=headers)
        response.raise_for_status()
        return redirect('event_detail', pk=pk)
    except requests.exceptions.RequestException as e:
        return HttpResponse(f"An error occurred: {e}", status=500)
    

def leave_event(request, pk):
    api_url = f'http://127.0.0.1:8000/api/leave/{pk}/'
    headers = {'Authorization': f'Bearer {request.session["auth_token"]}'}

    try:
        response = requests.post(api_url, headers=headers)
        response.raise_for_status()
        return redirect('event_detail', pk=pk)
    except requests.exceptions.RequestException as e:
        return HttpResponse(f"An error occurred: {e}", status=500)
