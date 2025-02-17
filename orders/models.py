import uuid

from django.db import models


#ORDER
class Order(models.Model):
  id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
  withdrawal_date = models.DateTimeField()
  comment = models.TextField()
  is_finished = models.BooleanField(default=False, null=True)
  total = models.DecimalField(max_digits=10, decimal_places=2, null=True)

  account = models.ForeignKey("accounts.Account", on_delete=models.CASCADE, related_name="orders")
  products = models.ManyToManyField("products.Product", through="orders.Order_Products" ,related_name="orders")

# Tabela pivô order_products
class Order_Products(models.Model):
  id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
  
  product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
  order = models.ForeignKey('orders.Order', on_delete=models.CASCADE)
  quantity = models.IntegerField()
