from django import forms

from .models import LockBoxStatusModel, ShippingInfoModel


class LockUnlockForm(forms.ModelForm):
    class Meta:
        model = LockBoxStatusModel
        fields = [
            "desiredLockStatus",
        ]


class ShippingInfoForm(forms.ModelForm):
    class Meta:
        model = ShippingInfoModel
        fields = [
            "item",
            "shippingNumber",
        ]
