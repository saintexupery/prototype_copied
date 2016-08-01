from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


UNIV_CHOICES = (
    (1, ("서울대학교")),
    (2, ("한양대학교")),
    (3, ("이화여자대학교")),
)

class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class AddedSignupForm(forms.ModelForm):
    university = forms.ChoiceField(
        required = True,
        choices = UNIV_CHOICES,
        widget = forms.Select(),
    )

    class Meta:
        model = UserProfile
        exclude = ['user']