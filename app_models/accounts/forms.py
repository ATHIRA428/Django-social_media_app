from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from model_setup .models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email','date_of_birth', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
