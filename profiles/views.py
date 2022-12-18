from django.shortcuts import render

# Create your views here.
from re import template
from django import forms
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from .form import RegistrationForm
from django.http import HttpResponseRedirect

# Create your views here.
class SiteLoginView(LoginView):
    template_name='login.html'

class EditProfileView(LoginRequiredMixin, TemplateView):
    template_name='profile.html'

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'register.html', {'form': form})




