from rest_framework import serializers

from .models import LockBoxStatusModel, ShippingInfoModel

# this serializer organizes json for box status, allows for locking and unclocking
# from website or application
class LockBoxStatusSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'id',
            'name',
            'lockStatus',
            'desiredLockStatus',
        ]
        model = LockBoxStatusModel

#this serializer is used to organize the retrieval of new
# shipping info. uses different serializer than detailshippinginfo serializer
# to allow for different info to be viewed
class ShippingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'item',
            'shippingNumber',
            'barCode',
        ]
        model = ShippingInfoModel

# serializer to view shipping info and delivers barcode and pin to be
# dropped in carrier shipping instructions
class DetailShipppingInfo_Serializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'item',
            'shippingNumber',
            'barCode',
            'pinCode'  #remove pin code no longer using
        ]
        model = ShippingInfoModel

#this serializer organizes the json for the app only
# serializer for lockbox codes is ShippingInfoSerializer
class ListActivity_Serializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'item',
            'shippingNumber',
            'barCode',
            'shippingStatus',
            'creationDate',
            'expectedDeliveryDate',
        ]
        model = ShippingInfoModel
