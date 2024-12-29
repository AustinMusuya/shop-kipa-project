from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.HomeView.as_view(), name="home" ),
    path('register/', views.SignUpView.as_view(), name="register"),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('accounts/profile/', views.ProfileView.as_view(), name='profile'),

    # path to product categories
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('categories/add/', views.CategoryCreateView.as_view(), name='category-add'),
    path('categories/<int:pk>/edit/', views.CategoryUpdateView.as_view(), name='category-edit'),
    path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category-delete'),

    # paths to products
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('products/add/', views.ProductCreateView.as_view(), name='product-add'),
    path('products/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='product-edit'),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product-delete'),
]
