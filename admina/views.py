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
        return render(req, "admina/login.html", {"fs": fs})


def index(req):
    province = Province.objects.filter(isShow=True)
    area = Area.objects.filter(isShow=True)
    users = User.objects.all().order_by("-loginTime")
    return render(req, "admina/index.html", {"province": province, "area": area, "users": users})


def getProvince(req):
    province = Province.objects.filter(isShow=True)
    data = serializers.serialize("json", province)
    return HttpResponse(data)


def getArea(req):
    area = Area.objects.filter(provinceId=req.GET['provinceId'], isShow=True)
    data = serializers.serialize("json", area)
    return HttpResponse(data)


def getUsers(req):
    users = User.objects.filter(isShow=True)
    data = []

    areaId = req.GET.get("areaId", "0")
    if areaId != "0":
        users = users.filter(areaId=areaId)

    orderByWay = {"0": "-loginTime", "1": "loginTime", "2": "-registerTime", "3": "registerTime",
                  "4": "-areaId__areaName", "5": "areaId__areaName", "6": "-userName", "7": "userName"}

    orderBy = orderByWay[req.GET["orderById"]]
    # orderBy = orderByWay[req.GET.get("orderById", "0")]
    users = users.order_by(orderBy)


    for user in users:
        info = {}
        info['userId'] = user.userId
        info['userName'] = user.userName
        info['areaName'] = user.areaId.areaName
        info['provinceName'] = user.areaId.provinceId.provinceName
        info['registerTime'] = user.registerTime.strftime("%Y-%m-%d-%H:%M:%S")
        info['loginTime'] = user.loginTime.strftime("%Y-%m-%d-%H:%M:%S")
        info['isShow'] = user.isShow
        data.append(info)
    return HttpResponse(json.dumps(data))