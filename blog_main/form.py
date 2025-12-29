from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationFrom(UserCreationForm):
    class Meta:
        model = User
        fields = {'username','email'}
    