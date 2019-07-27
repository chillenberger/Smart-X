from django.contrib import admin

# Register your models here.
from .models import LockBoxStatusModel, ShippingInfoModel

admin.site.register(LockBoxStatusModel)
admin.site.register(ShippingInfoModel)
