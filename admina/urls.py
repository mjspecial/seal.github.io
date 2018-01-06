from django.conf.urls import url
from views import login, index, getProvince

urlpatterns = [
    url(r'^login$', login),
    url(r'^index/', index),

    url(r'^getProvince$', getProvince),
]