from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from .models import Orders, OrderDetail

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['supplier', 'status', 'total_amount']

OrderDetailFormset = inlineformset_factory(
    Orders,
    OrderDetail,
    fields=['product', 'quantity_ordered', 'unit_price'],
    extra=1,
    can_delete=True
)