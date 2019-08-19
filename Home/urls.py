from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.views.generic import TemplateView

from .views import ShippingInfoOutput

#static page urls
urlpatterns = [
    url('sign_in_Smart-x/$', TemplateView.as_view(template_name='sign_in.html'), name='sign_in'),
    # url('signed_in/$', TemplateView.as_view(template_name='signed_in.html'), name='signed_in'),
    url(r'^API/LockBoxStatus/$', views.ListLockBoxStatus_API.as_view()),
    url(r'^API/LockBoxStatus/(?P<pk>[-\w]+)/$', views.DetailLockBoxStatus_API.as_view()),
    url(r'^API/shippinginfo/$', views.ShippingInfo_API.as_view()),
    url(r'^API/DetailShipppingInfo_API/(?P<pk>[-\w]+)/$', views.DetailShipppingInfo_API.as_view()),
    url(r'^API/ListActivity/$', views.ListActivity_API.as_view()),


    url(r'^signed_in/shippinginfo/new_shipment/$', views.ShippingInfoNewView, name="shippinginfonew"),
    url(r'^signed_in/shippinginfo/output/(?P<pk>[-\w]+)/$', views.ShippingInfoOutput.as_view(), name="shippinginfoout"),
    url(r'^signed_in/$', views.LockUnlockView, name="signed_in"),


    url(r'^', TemplateView.as_view(template_name='home.html'), name='home'),
]
