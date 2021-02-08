from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls import url, include


urlpatterns =[
    url(r'^hotel_image_view/$',views.hotel_image_view,name='hotel_image_view'),
    url(r'^success/$',views.success,name='success'),
    url(r'^myproduct/$',views.myproduct,name='myproduct'),
    url(r'^removemyproduct/$',views.removemyproduct,name='removemyproduct'),
    path('setsession/<category>/<city>/',views.setsession),
    path('setsession1/<category>/',views.setsession1),
    path('productditail/<id>/',views.productditail),
    url(r'^addtocart/$',views.addtocart,name='addtocart'),
    url(r'^mycart/$',views.mycart,name='mycart'),
    url(r'^removeformcart/$',views.removeformcart,name='removeformcart'),
    url(r'^myprofile/$',views.myprofile,name='myprofile'),
    url(r'^updateprofileform/$',views.updateprofileform,name='updateprofileform'),
    url(r'^updateprofile/$',views.updateprofile,name='updateprofile'),
    

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#if settings.DEBUG:
 #   urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)