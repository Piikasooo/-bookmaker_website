from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import RegistrationForm


def user_registration(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            print(form)
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password1'],
                                email=form.cleaned_data['email'])
            login(request, user)
            return redirect('home')
    return render(request, 'user/registration.html', {"form": form} )