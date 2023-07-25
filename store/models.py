import datetime
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class category(models.Model):
    name = models.CharField(max_length=25, null=False, blank=False)

    def get_all_categories():
        return category.objects.all()

    def __str__(self):
        return self.name





class product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(category, on_delete=models.CASCADE, default=1)
    price = models.IntegerField()
    description = models.CharField(max_length=150, blank=True, null=True)
    image = models.ImageField(upload_to='uploads/products/')

    def get_product_by_id(id):
        return product.objects.filter(id__in=id)

    def get_all_products():
        return product.objects.all()

    def get_all_products_by_categoryid(category_id):
        if category_id:
            return product.objects.filter(category=category_id)
        else:
            return product.get_all_products()

    def __str__(self):
        return self.name


class order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=6)

    def __str__(self):
        return str(self.order_id)


class orderTracker(models.Model):
    updateId = models.AutoField(primary_key=True)
    orderId = models.IntegerField()
    updateDesc = models.CharField(max_length=1000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.updateDesc[0:15]+"..."
