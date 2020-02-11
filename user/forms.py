from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                             'placeholder': 'your unique login'
                                                                             }))
    email = forms.EmailField( widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                           'placeholder': 'example@mail.com'
                                                                           }))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                 'placeholder': 'password'
                                                                                 }))
    confirm_password = forms.CharField(label="Password confirm",widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                 'placeholder': 'confirm password'
                                                                                 }))
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')


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