from django import forms
from users.models import City

class SearchUserForm(forms.Form):
    city = forms.ModelChoiceField(queryset=City.objects.all(), required=True)