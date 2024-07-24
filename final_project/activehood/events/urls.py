from django.urls import path
from . import api_views, views

urlpatterns = [
    path("", api_views.EventListByLocation.as_view(), name="api_events_home"), 
    path("create/", api_views.CreateEvent.as_view(), name='api_events_create'),
    path('<int:pk>/', api_views.EventDetail.as_view(), name='api_events_detail'),
    path('myevents/', api_views.MyEventsList.as_view(), name='api_events_myevents'),
    path('participating/', api_views.MyParticipationList.as_view(), name='api_events_participating'), 
    path('user/<int:user_id>/', api_views.UserEventsList.as_view(), name='api_events_userevents'),
    path('join/<int:pk>/', api_views.JoinEvent.as_view(), name='api_events_join'),
    path('leave/<int:pk>/', api_views.LeaveEvent.as_view(), name='api_events_leave'),
    # regular views
    #path('display/', views.display_event, name='display'),
]
