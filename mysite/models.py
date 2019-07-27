from django.db import models

# Required for unique book instances
import uuid

# Will be used to create users update in the future
from django.contrib.auth.models import User
from datetime import datetime
from mysite.python.functions import codeCreator, codGenerator

#used to populate info afert submited
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver



# this model is used to track the state of the lockbox.
class LockBoxStatusModel(models.Model):
    """
    Model for lockbox state
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this product")
    name = models.CharField(max_length = 40, help_text = "LockBoxName")
    lockStatus = models.BooleanField(default=True)        #true means is locked
    desiredLockStatus = models.BooleanField(default=True) #false means is desired locked, default low value means lock on loss of power


    #Return a string representing the model
    def __str__(self):
        return self.name




class ShippingInfoModel(models.Model):
    """
    Model for all ShippingInfoForm
    """

    item = models.CharField(default = 'Not Specified', max_length = 40, help_text = "Purchased Item")
    shippingNumber = models.CharField(max_length = 40, help_text ="Shipping number from Carrier")
    shippingStatus = models.CharField(default = "Shipped", blank = True, null = True, max_length = 100) #change default to not shipped in real code
    creationDate = models.DateTimeField(default=datetime.now())
    expectedDeliveryDate = models.DateTimeField(blank = True, null = True)
    barCode = models.CharField(max_length = 120, blank = True, null = True)
    # barCodeReadable = models.CharField(max_length = 120, blank = True, null = True) #look into needing this and how we will render barcode
    # pinCode = models.CharField(max_length = 9, blank = True, null = True)  #remove pin code no longer used

    #Return a string to represent model
    def __str__(self):
        return self.item

    #this code is called prior to model being made to call python code to make
    # the barcode
    def save(self, *args, **kwargs):
        if not self.pk:
            print('in reciever funciotn')
            print(self.id)
            # code = codeCreator()
            code = codGenerator(2,4)
            self.barCode = code
            # self.barCode = code.barCode
            # self.barCodeReadable = code.readableCode
            # self.pinCode = code.pinCode
            self.pk = self.shippingNumber
        super(ShippingInfoModel, self).save(*args, **kwargs)
