from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import RegisterForm, LoginForm


def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data.get('password'))
            new_user.is_active = True
            new_user.save()
            data = form.cleaned_data
            user = authenticate(request, email=data['email'], password=data['password'])
            login(request, user)

            return redirect("anime:index")

    form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, email=data['email'], password=data['password'])
            login(request, user)
            return redirect("anime:index")

    form = LoginForm()
    return render(request, 'users/login.html', {'form': form})
