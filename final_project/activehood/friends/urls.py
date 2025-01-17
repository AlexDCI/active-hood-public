from django.urls import path
from friends.views import  view_friend_requests, send_friend_request, accept_friend_request, search_users, add_friend, user_profile, remove_friend


app_name = 'friends'

urlpatterns = [
    # path('members/', user_all_list, name='user_list'),
    path('profile/<str:username>/', user_profile, name='user_profile'),
    path('remove_friend/<int:user_id>/', remove_friend, name='remove_friend'),
    # path('users/', user_list, name='user_list'),
    path('send_friend_request/<int:user_id>/', send_friend_request, name='send_friend_request'),
    path('friend_requests/', view_friend_requests, name='friend_requests'),
    path('accept_friend_request/<int:request_id>/', accept_friend_request, name='accept_friend_request'),

    path('citys/', search_users, name='search_users'),
    path('add_friend/<int:user_id>/', add_friend, name='add_friend'),
    
   

]
