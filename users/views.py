from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages

from .forms import RegisterForm, LoginForm, UserEditForm, UserProfileEditForm
from .models import CustomUser, Profile


class UserRegister(CreateView):
    model = CustomUser
    template_name = 'users/register.html'
    form_class = RegisterForm

    def form_valid(self, form):
        request = self.request
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data.get('password'))
        new_user.is_active = True
        new_user.save()
        data = form.cleaned_data
        user = authenticate(request, email=data['email'], password=data['password'])
        if user is not None:
            login(request, user)
            Profile.objects.create(user=user)
            messages.success(request, "Акаунт створено!")
            return redirect("anime:index")
        return super().form_valid(form)


class UserLogin(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'

    def form_valid(self, form):
        messages.success(self.request, "Ви успішно ввійшли.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Перевірте дані для входу.")
        return super().form_invalid(form)


class UserLogout(LoginRequiredMixin, LogoutView):
    next_page = 'anime:index'


class UserProfile(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = "users/profile.html"
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user


class UserSettings(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'users/settings.html'
    success_url = reverse_lazy('user:settings')

    def get_object(self):
        return self.request.user

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_user = UserEditForm(instance=self.request.user)
        form_profile = UserProfileEditForm(instance=self.request.user.profile)
        return self.render_to_response(self.get_context_data(form_user=form_user, form_profile=form_profile))


class UserEdit(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = 'users/settings.html'
    form_class = UserEditForm
    success_url = reverse_lazy('user:settings')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Успішно оновлено!")
        return super().form_valid(form)


class UserProfileEdit(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = UserProfileEditForm
    template_name = 'users/settings.html'
    success_url = reverse_lazy('user:settings')

    def get_object(self, queryset=None):
        return self.request.user.profile

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Успішно оновлено!")
        return super().form_valid(form)
