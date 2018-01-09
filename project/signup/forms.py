from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    Male = 'ML'
    Female = 'FM'
    GenderChoices = (
        (Male, 'Male'),
        (Female, 'Female'),
    )
    gender = forms.ChoiceField(widget=forms.Select, choices=GenderChoices)
    address = forms.CharField(max_length=100, widget=forms.Textarea)

    class Meta:
        model = User
        fields = ['username', 'gender', 'address', 'password1', 'password2']