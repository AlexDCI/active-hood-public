from django.urls import path
from users.views import home, RegisterView, CustomLoginView    # Import the view here
from django.contrib.auth import views as auth_views
from users.forms import LoginForm


urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),  # This is what we added
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='users/login.html',
                                          authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
    