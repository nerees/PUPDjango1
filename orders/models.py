from django.db import models
import datetime

class Customer(models.Model):
    f_name = models.CharField(max_length=250)
    l_name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.f_name} {self.l_name}'


class Status(models.Model):
    id = models.IntegerField(unique=1, primary_key=1)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.IntegerField(unique=1, primary_key=1)
    name = models.CharField(max_length=250)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now=True, editable=False)
    status_id = models.ForeignKey(Status, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.date.strftime("%Y-%m-%d")} | {self.customer_id} | {self.status_id} | '
        # return f'{datetime.datetime.strptime(str(self.date), "%Y-%m-%d %H:%M:%S")} {str(self.status_id)}'



class ProductOrder(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.order_id)