from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .forms import RegisterForm
from .models import Category
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.

class HomeView(TemplateView):
    template_name = 'main/base.html'

class SignUpView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"


class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'    

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff  # Only staff can access

class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'categories/category-list.html'
    context_object_name = 'categories'

class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category
    template_name = 'categories/category-detail.html'
    context_object_name = 'category'

class CategoryCreateView(AdminRequiredMixin, CreateView):
    model = Category
    template_name = 'categories/category-form.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('category-list')

class CategoryUpdateView(AdminRequiredMixin, UpdateView):
    model = Category
    template_name = 'categories/category-form.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('category-list')

class CategoryDeleteView(AdminRequiredMixin, DeleteView):
    model = Category
    template_name = 'categories/category-confirm-delete.html'
    success_url = reverse_lazy('category-list')
