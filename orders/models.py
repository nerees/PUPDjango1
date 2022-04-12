from django.db import models
import datetime

class Customer(models.Model):
    f_name = models.CharField(max_length=250)
    l_name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return f'{self.f_name} {self.l_name}'


class Status(models.Model):
    id = models.IntegerField(unique=1, primary_key=1)
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.IntegerField(unique=1, primary_key=1)
    name = models.CharField(max_length=250)
    price = models.FloatField(default=0.0)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name

    def __str__(self):
        return f'{self.name} - {self.price}'


class Order(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now=True, editable=False)
    status_id = models.ForeignKey(Status, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def total_quantity(self):
        product_orders = ProductOrder.objects.filter(order_id=self)
        total = 0
        for order in product_orders:
            total = total + order.quantity

        return total

    def total_order_price(self):
        product_orders = ProductOrder.objects.filter(order_id=self)
        total_price = 0
        for order in product_orders:
            total_price = total_price + order.quantity * order.product_id.price

        return total_price

    def __str__(self):
        return f'{self.date.strftime("%Y-%m-%d")} | {self.customer_id} | {self.status_id} ' \
               f'| TOTAL products: {self.total_quantity()} | ORDER TOTAL PRICE: {self.total_order_price()} EUR'


class ProductOrder(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'ProductOrder'
        verbose_name_plural = 'ProductOrders'

    def __str__(self):
        return f'{self.product_id}'