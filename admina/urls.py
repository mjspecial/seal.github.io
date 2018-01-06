from django.conf.urls import url
from views import login, index, getProvince, getArea, getUsers

urlpatterns = [
    url(r'^login$', login),
    url(r'^index/', index),

    url(r'^getProvince$', getProvince),
    url(r'^getArea$', getArea),
    url(r'^getUsers$', getUsers),
]