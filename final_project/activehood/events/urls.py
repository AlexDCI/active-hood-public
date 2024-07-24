from django.urls import path
from . import api_views, views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("api/", api_views.EventListByLocation.as_view(), name="api_events_home"), 
    path("api/create/", api_views.CreateEvent.as_view(), name='api_create_event'),
    path('api/<int:pk>/', api_views.EventDetail.as_view(), name='api_event_detail'),
    path('api/myevents/', api_views.MyEventsList.as_view(), name='api_events_myevents'),
    path('api/participating/', api_views.MyParticipationList.as_view(), name='api_events_participating'), 
    path('api/user/<int:user_id>/', api_views.UserEventsList.as_view(), name='api_events_userevents'),
    path('api/join/<int:pk>/', api_views.JoinEvent.as_view(), name='api_join_event'),
    path('api/leave/<int:pk>/', api_views.LeaveEvent.as_view(), name='api_leave_event'),
    path('api/token/', TokenObtainPairView.as_view(), name = 'Token obtain pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name= 'token refresh'),

    # regular views
#    path("", views.events_list, name="events_home"), 
    path("create/", views.create_event, name='create_event'),
    path('<int:pk>/', views.event_detail, name='event_detail'),
    path('join/<int:pk>/', views.join_event, name='join_event'),
    path('leave/<int:pk>/', views.leave_event, name='leave_event'),
]
