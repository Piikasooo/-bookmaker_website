from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Account created for {username}!')
            messages.success(request, f'Login as {username}!')
            return redirect('user/home')
    else:
        form = RegistrationForm()
    return render(request, 'user/register.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                messages.success(request, f'Login as {username}!')
                return redirect('/user/login')
            else:
                messages.error(request, f'Invalid login for {username}!')
                return redirect('/user/login')
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form': form})


def home(request):
    return render(request, 'user/base.html')

