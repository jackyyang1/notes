from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^fan1$', views.fan1),
    url(r'^fan2222$', views.fan2, name='fan2'),
    url(r'^red1$', views.red1),
    url(r'^red2$', views.red2),
    url(r'^fan3/(\d+)/(\d+)$', views.fan3, name='fan3'),
    url(r'^jingtai$', views.jingtai),
    url(r'^mid$', views.mid),
    url(r'^pic_upload$', views.pic_upload),
    url(r'^pic_handle$', views.pic_handle),
    url(r'^pic_show$', views.pic_show),
    url(r'^pagelist(\d*)$', views.pagelist),
    url(r'^area_select$', views.area_select),
    url(r'^area$', views.area),


]