from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import UpdateView

#for rest api framwork
from rest_framework import generics
from .serializers import ( LockBoxStatusSerializer,
                            ShippingInfoSerializer,
                            DetailShipppingInfo_Serializer,
                            ListActivity_Serializer)

#for my funcitons
from .models import LockBoxStatusModel, ShippingInfoModel

#for my forms
from .forms import LockUnlockForm, ShippingInfoForm
from django.http import HttpResponseRedirect
from django.urls import reverse


#following view are for locking and unclocking box
# this view is the LockBox lock/unlock rest_framework view
class DetailLockBoxStatus_API(generics.RetrieveUpdateDestroyAPIView): #try to combine with view below
    queryset = LockBoxStatusModel.objects.all()
    serializer_class = LockBoxStatusSerializer

#for user to read status of lockbox on application and Gateway
class ListLockBoxStatus_API(generics.ListCreateAPIView): #dosnt need create ability
    queryset = LockBoxStatusModel.objects.all()
    serializer_class = LockBoxStatusSerializer

#Relocking is done by a timer from the lockbox embeded software. It will
#update the website on box status as locked or unlocked
def LockUnlockView(request):
        #if post request process the form
    if request.method == 'POST':
        #remove this hardcoded pk
        #this will be a key associated with the specific user profile
        object = LockBoxStatusModel.objects.get(pk='a8124a5e-6077-49ee-a976-71fae9b6e8a8')

        form = LockUnlockForm(request.POST, instance=object)

        form.save()
        print(object.desiredLockStatus)
        return HttpResponseRedirect(reverse('signed_in'))

        # add form validation

    else:
        form = LockUnlockForm()
        return render(request, 'signed_in.html', {'form': form})




#following views are to support shipping info
# this is the restfull framework so the box knows active codes to allow unlocking
class ShippingInfo_API(generics.ListCreateAPIView):
    queryset = ShippingInfoModel.objects.filter(shippingStatus__exact='Shipped')
    serializer_class = ShippingInfoSerializer

class DetailShipppingInfo_API(generics.RetrieveAPIView):
    queryset = ShippingInfoModel.objects.all()
    serializer_class = DetailShipppingInfo_Serializer

class ShippingInfoOutput(generic.DetailView):
    model = ShippingInfoModel
    template_name = "shippingout.html"

#views to support Shipping submition from Website and application
def ShippingInfoNewView(request):
    #if post request process the form
    if request.method == 'POST':
        print("in post for shipping info view")
        print(request.POST)
        form = ShippingInfoForm(request.POST)
        new_object = form.save() #return the object so we can call the pk and return the specific itme html
        return HttpResponseRedirect(reverse('shippinginfoout', args=(new_object.pk,)))

    else:
        print("/n /n in shipping info form /n /n")
        form = ShippingInfoForm()
        return render(request, 'shippingInfoNew.html', {'form': form})


# full activit detail list views are below.
# this will the the Detailview for the website
#(not yet made)

#This is the restfull famework to suppor viewing Box activity on opp
class ListActivity_API(generics.ListAPIView):
    queryset = ShippingInfoModel.objects.all()
    serializer_class = ListActivity_Serializer
