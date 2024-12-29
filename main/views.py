from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .forms import RegisterForm, OrdersForm
from .models import Category, Product, Supplier, SaleDetail, Sales, OrderDetail, Orders
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.forms import inlineformset_factory

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
    template_name = 'suppliers/supplier-list.html'
    context_object_name = 'suppliers'


class SupplierDetailView(LoginRequiredMixin, DetailView):
    model = Supplier
    template_name = 'suppliers/supplier-detail.html'
    context_object_name = 'supplier'


class SupplierCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Supplier
    fields = ['name', 'contact_number', 'email', 'address']
    template_name = 'suppliers/supplier-form.html'
    success_url = reverse_lazy('supplier-list')


class SupplierUpdateView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = Supplier
    fields = ['name', 'contact_number', 'email', 'address']
    template_name = 'suppliers/supplier-form.html'
    success_url = reverse_lazy('supplier-list')


class SupplierDeleteView(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
    model = Supplier
    template_name = 'suppliers/supplier-confirm-delete.html'
    success_url = reverse_lazy('supplier-list')


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
    template_name = 'sales/sales-list.html'
    context_object_name = 'sales'


class SalesDetailView(LoginRequiredMixin, DetailView):
    model = Sales
    template_name = 'sales/sales-detail.html'
    context_object_name = 'sale'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sale_details'] = self.object.details.all()  # Fetch related SaleDetail items
        return context


class SalesCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Sales
    fields = ['total_amount']
    template_name = 'sales/sales-form.html'
    success_url = reverse_lazy('sales-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        SaleDetailFormSet = inlineformset_factory(Sales, SaleDetail, fields=('product', 'quantity_sold', 'selling_price'), extra=1)
        context['formset'] = SaleDetailFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)


class SalesUpdateView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = Sales
    fields = ['sale_date', 'total_amount']
    template_name = 'sales/sales-form.html'
    success_url = reverse_lazy('sales-list')


class SalesDeleteView(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
    model = Sales
    template_name = 'sales/sales-confirm-delete.html'
    success_url = reverse_lazy('sales-list')


# Orders Views

class OrderListView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    model = Orders
    template_name = 'orders/order-list.html'
    context_object_name = 'orders'


class OrderCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Orders
    form_class = OrdersForm
    template_name = 'orders/order-form.html'
    success_url = reverse_lazy('orders-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        OrderDetailFormset = inlineformset_factory(
            Orders, OrderDetail,
            fields=['product', 'quantity_ordered', 'unit_price'],
            extra=1, can_delete=True
        )
        if self.request.POST:
            context['formset'] = OrderDetailFormset(self.request.POST)
        else:
            context['formset'] = OrderDetailFormset()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.success_url)
        else:
            return self.form_invalid(form)


class OrderUpdateView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = Orders
    form_class = OrdersForm
    template_name = 'orders/order-form.html'
    success_url = reverse_lazy('orders-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        OrderDetailFormset = inlineformset_factory(
            Orders, OrderDetail,
            fields=['product', 'quantity_ordered', 'unit_price'],
            extra=1, can_delete=True
        )
        if self.request.POST:
            context['formset'] = OrderDetailFormset(self.request.POST, instance=self.object)
        else:
            context['formset'] = OrderDetailFormset(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.success_url)
        else:
            return self.form_invalid(form)

class OrderDeleteView(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
    model = Orders
    template_name = 'orders/order-confirm-delete.html'
    success_url = reverse_lazy('orders-list')
