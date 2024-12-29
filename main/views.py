from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .forms import RegisterForm
from .models import Category, Product, Supplier, SaleDetail, Sales, OrderDetail
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


# Supplier Views
class SupplierListView(LoginRequiredMixin, ListView):
    model = Supplier
    template_name = 'supplier_list.html'
    context_object_name = 'suppliers'


class SupplierDetailView(LoginRequiredMixin, DetailView):
    model = Supplier
    template_name = 'supplier_detail.html'
    context_object_name = 'supplier'


class SupplierCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Supplier
    fields = ['name', 'contact_number', 'email', 'address']
    template_name = 'supplier_form.html'
    success_url = reverse_lazy('supplier_list')


class SupplierUpdateView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = Supplier
    fields = ['name', 'contact_number', 'email', 'address']
    template_name = 'supplier_form.html'
    success_url = reverse_lazy('supplier_list')


class SupplierDeleteView(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
    model = Supplier
    template_name = 'supplier_confirm_delete.html'
    success_url = reverse_lazy('supplier_list')


# Product Views
class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'products/product-list.html'
    context_object_name = 'products'

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'products/product-detail.html'
    context_object_name = 'product'

class ProductCreateView(AdminRequiredMixin, CreateView):
    model = Product
    template_name = 'products/product-form.html'
    fields = ['name', 'price', 'quantity_in_stock', 'reorder_level', 'unit', 'description', 'category', 'supplier']
    success_url = reverse_lazy('product-list')

class ProductUpdateView(AdminRequiredMixin, UpdateView):
    model = Product
    template_name = 'products/product-form.html'
    fields = ['name', 'price', 'quantity_in_stock', 'reorder_level', 'unit', 'description', 'category', 'supplier']
    success_url = reverse_lazy('product-list')

class ProductDeleteView(AdminRequiredMixin, DeleteView):
    model = Product
    template_name = 'products/product-confirm-delete.html'
    success_url = reverse_lazy('product-list')


# Sales views
class SalesListView(LoginRequiredMixin, ListView):
    model = Sales
    template_name = 'sales_list.html'
    context_object_name = 'sales'


class SalesDetailView(LoginRequiredMixin, DetailView):
    model = Sales
    template_name = 'sales_detail.html'
    context_object_name = 'sale'


class SalesCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Sales
    fields = ['sale_date', 'total_amount']
    template_name = 'sales_form.html'
    success_url = reverse_lazy('sales_list')


class SalesUpdateView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = Sales
    fields = ['sale_date', 'total_amount']
    template_name = 'sales_form.html'
    success_url = reverse_lazy('sales_list')


class SalesDeleteView(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
    model = Sales
    template_name = 'sales_confirm_delete.html'
    success_url = reverse_lazy('sales_list')