from django.contrib import admin
from .models import product, category, order, orderTracker
# # Register your models here.
admin.site.register(product)
admin.site.register(category)
admin.site.register(order)
admin.site.register(orderTracker)
