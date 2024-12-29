from django.db import models
from django.core.validators import RegexValidator


# Create your models here.

phone_validator = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
)

class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.name

class Sales(models.Model):
    sale_date = models.DateTimeField(auto_now=True)
    total_amount = models.FloatField()

    def __str__(self):
        return f"Sale on {self.sale_date} - Total: {self.total_amount}"


class Supplier(models.Model):
    name = models.CharField(max_length=150)
    contact_number =  models.CharField(validators=[phone_validator], max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=254)
    address = models.TextField()

    def __str__(self):
        return self.name

class Orders(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='supplier_order')
    order_date = models.DateField(auto_now=True)
    total_amount = models.FloatField()
    status = models.CharField(max_length=150)

class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    quantity_in_stock = models.PositiveIntegerField()
    reorder_level = models.PositiveIntegerField()
    unit = models.CharField(max_length=150) 
    description = models.TextField()
    date_added = models.DateTimeField(auto_now=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="product_supplier")

    def __str__(self):
        return self.name

class OrderDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_order")
    quantity_ordered = models.PositiveIntegerField()
    unit_price = models.FloatField()
    orders = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name='details')


class SaleDetail(models.Model):
    sale = models.ForeignKey(Sales, on_delete=models.CASCADE, related_name="sale")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_sale")
    quantity_sold = models.PositiveIntegerField()
    selling_price = models.FloatField()

    def __str__(self):
        return f"{self.product.name} - Quantity: {self.quantity_sold} - Price: {self.selling_price}"