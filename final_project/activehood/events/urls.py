from django.urls import path
from . import views
#from .views import 

urlpatterns = [
    path("", views.EventListByLocation.as_view(), name="events_home"),
    path("create/", views.CreateEvent.as_view(), name='create_event'),
    path('<int:pk>/', views.EventDetail.as_view(), name='event_detail'),
    path('myevents/', views.MyEventsList.as_view(), name='myevents'),
]
