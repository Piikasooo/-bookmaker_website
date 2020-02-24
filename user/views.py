from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import RegistrationForm, UserProfileForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def register(request):
    print('+')
    if request == 'POST':
        form = UserCreationForm(request.POST)
        print('пройшло')
        if form.is_valid():
            print('не пройшло')
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('test')
    else:
        form = UserCreationForm()
    return render(request, 'user/register.html', {'form': form})


def test(request):
    return render(request, 'user/base.html')

'''
def user_registration(request):
    user_form = RegistrationForm()
    profile_form = UserProfileForm()
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            print(user_form)
            user = user_form.save()
            profile = UserProfileForm(commit=False)
            print(profile_form)
            profile.user = user
            profile.save()
            messages.success(request, 'Successful registration')
            return redirect('user/registration.html')
    return render(request, 'user/registration.html', {"user_form": user_form,
                                                      "profile_form": profile_form,
                                                      } )
'''

