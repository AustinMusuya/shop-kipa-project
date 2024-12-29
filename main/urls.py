from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Paths to Registration and Login URLs
    path('', views.HomeView.as_view(), name="home" ),
    path('register/', views.SignUpView.as_view(), name="register"),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('accounts/profile/', views.ProfileView.as_view(), name='profile'),

    # Paths to Product-Categories URLs
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('categories/add/', views.CategoryCreateView.as_view(), name='category-add'),
    path('categories/<int:pk>/edit/', views.CategoryUpdateView.as_view(), name='category-edit'),
    path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category-delete'),

    # Paths to Supplier URLs
    path('suppliers/', views.SupplierListView.as_view(), name='supplier-list'),
    path('suppliers/<int:pk>/', views.SupplierDetailView.as_view(), name='supplier-detail'),
    path('suppliers/add/', views.SupplierCreateView.as_view(), name='supplier-add'),
    path('suppliers/<int:pk>/edit/', views.SupplierUpdateView.as_view(), name='supplier-edit'),
    path('suppliers/<int:pk>/delete/', views.SupplierDeleteView.as_view(), name='supplier-delete'),


    # Paths to Products URLs
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('products/add/', views.ProductCreateView.as_view(), name='product-add'),
    path('products/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='product-edit'),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product-delete'),

    # Paths to Sales URLs
    path('sales/', views.SalesListView.as_view(), name='sales-list'),
    path('sales/<int:pk>/', views.SalesDetailView.as_view(), name='sales-detail'),
    path('sales/add/', views.SalesCreateView.as_view(), name='sales-create'),
    path('sales/<int:pk>/edit/', views.SalesUpdateView.as_view(), name='sales-edit'),
    path('sales/<int:pk>/delete/', views.SalesDeleteView.as_view(), name='sales-delete'),


    # Paths to Orders URLs
    path('orders/', views.OrderListView.as_view(), name='orders-list'),
    path('orders/add/', views.OrderCreateView.as_view(), name='order-add'),
    path('orders/<int:pk>/edit/', views.OrderUpdateView.as_view(), name='order-edit'),
    path('orders/<int:pk>/delete/', views.OrderDeleteView.as_view(), name='order-delete'),
]
