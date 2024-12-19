from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import RegisterForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.

class HomeView(TemplateView):
    template_name = 'main/base.html'

class SignUpView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"

    