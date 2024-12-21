from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.HomeView.as_view(), name="home" ),
    path('register/', views.SignUpView.as_view(), name="register"),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('accounts/profile/', views.ProfileView.as_view(), name='profile'),
]
