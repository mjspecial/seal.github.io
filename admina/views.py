# -*- utf-8:coding -*-

from __future__ import unicode_literals

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from forms import LoginForm
from users.models import Province, Area, User
import json


def login(req):
    if req.method == "GET":
        fs = LoginForm()
        return render(req, "admina/login.html", {"fs":fs})


def index(req):
    province = Province.objects.filter(isShow=True)
    area = Area.objects.filter(isShow=True)
    users = User.objects.all().order_by("-loginTime")
    return render(req, "admina/index.html", {"province": province, "area": area, "users": users})


def getProvince(req):
    province = Province.objects.filter(isShow=True)
    data = serializers.serialize("json", province)
    return HttpResponse(data)
