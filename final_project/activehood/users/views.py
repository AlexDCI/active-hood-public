from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.urls import reverse_lazy
from users.forms import UserRegisterForm, UserPasswordResetForm, UserSetPasswordForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username or password'})
    return render(request, 'users/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


class UserPasswordResetView(PasswordResetView):
    form_class = UserPasswordResetForm
    success_url = reverse_lazy('password_reset_done')
    template_name = 'users/password_reset.html'

class UserPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = UserSetPasswordForm
    success_url = reverse_lazy('password_reset_complete')
    template_name = 'users/password_reset_confirm.html'

@login_required
def home(request):
    return render(request, 'users/home.html')

