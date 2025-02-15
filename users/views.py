from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView, PasswordResetView

# Create your views here.
class MyPasswordChangeView(PasswordChangeView):
    template_name = 'users/password-change.html'
    success_url = reverse_lazy('users:users.password-change-done-view')

class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password-reset-done.html'