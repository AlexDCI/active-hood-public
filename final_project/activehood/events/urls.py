from django.urls import path
from . import views

urlpatterns = [
    path("", views.EventListByLocation.as_view(), name="events_home"), # needs update
    path("create/", views.CreateEvent.as_view(), name='events_create'),
    path('<int:pk>/', views.EventDetail.as_view(), name='events_detail'),
    path('myevents/', views.MyEventsList.as_view(), name='events_myevents'),
    path('participating/', views.MyParticipationList.as_view(), name='events_participating'), 
    path('user/<int:user_id>/', views.UserEventsList.as_view(), name='events_userevents'),
    path('join/<int:pk>/', views.JoinEvent.as_view(), name='events_join'),
    path('leave/<int:pk>/', views.LeaveEvent.as_view(), name='events_leave'),
]
