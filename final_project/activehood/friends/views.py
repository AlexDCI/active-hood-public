# friends/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from friends.models import FriendRequest
from friends.forms import SearchUserForm
from users.models import Profile, City

# @login_required
# def user_all_list(request):
#     users = User.objects.exclude(id=request.user.id)
#     return render(request, 'friends/members.html', {'users': users})

# @login_required
# def user_list(request):
#     users = User.objects.exclude(id=request.user.id)
#     friend_requests_sent = FriendRequest.objects.filter(from_user=request.user).values_list('to_user_id', flat=True)
#     friends = request.user.profile.friends.all()
#     return render(request, 'friends/user_list.html', {
#         'users': users,
#         'friend_requests_sent': friend_requests_sent,
#         'friends': friends
#     })

@login_required
def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'friends/user_profile.html', {'user': user})


@login_required
def send_friend_request(request, user_id):
    to_user = get_object_or_404(User, id=user_id)
    if request.user != to_user:
        friend_request, created = FriendRequest.objects.get_or_create(from_user=request.user, to_user=to_user)
    return redirect('friends:search_users')

@login_required
def view_friend_requests(request):
    # Получаем все запросы на добавление в друзья, которые отправлены текущему пользователю
    friend_requests = FriendRequest.objects.filter(to_user=request.user)
    
    # Получаем все друзья текущего пользователя
    friends = request.user.profile.friends.all()
    
    # Выбираем только те запросы, которые еще не приняты
    new_requests = friend_requests.exclude(from_user__profile__in=friends)

    # Отображаем список всех друзей, которые есть у текущего пользователя
    friends_list = request.user.profile.friends.all()

    return render(request, 'friends/friend_requests.html', {
        'new_requests': new_requests,
        'friends_list': friends_list
    })

# def view_friend_requests(request):
#     friend_requests = FriendRequest.objects.filter(to_user=request.user)
#     return render(request, 'friends/friend_requests.html', {'friend_requests': friend_requests})

@login_required
def accept_friend_request(request, request_id):
    friend_request = get_object_or_404(FriendRequest, id=request_id)
    if friend_request.to_user == request.user:
        request.user.profile.friends.add(friend_request.from_user.profile)
        friend_request.from_user.profile.friends.add(request.user.profile)
        friend_request.delete()
    return redirect('friends:friend_requests')


User = get_user_model()

@login_required
def search_users(request):
    if request.method == 'POST':
        form = SearchUserForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            users = User.objects.filter(profile__city=city).exclude(id=request.user.id)
            return render(request, 'friends/search_results.html', {'users': users, 'form': form})
    else:
        form = SearchUserForm()
    return render(request, 'friends/search.html', {'form': form})

@login_required
def add_friend(request, user_id):
    user_to_add = get_object_or_404(User, id=user_id)
    request.user.profile.friends.add(user_to_add.profile)
    return redirect('friends:search_users')
