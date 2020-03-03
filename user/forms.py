from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class RegistrationForm(UserCreationForm):
    #username = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    #password = forms.CharField(label="Password")
    #confirm_password = forms.CharField(label="Password confirm")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserProfileForm(forms.ModelForm):
    birthday = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control',
                                                             'placeholder': '31.12.1992'
                                                             }))
    avatar = forms.FileField(required=False, widget=forms.FileInput(attrs={'class': 'custom-file-input',
                                                             'id': 'avatar_input'
                                                             }))

    class Meta:
        model = UserProfile
        fields = ('birthday', 'avatar')
