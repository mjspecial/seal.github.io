# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

yes_or_no = (
    (True, "是"),
    (False, "否")
)


@python_2_unicode_compatible
class Province(models.Model):
    provinceId = models.AutoField(primary_key=True)
    provinceName = models.CharField(max_length=20)
    isShow = models.BooleanField("是否启用", choices=yes_or_no, default=True)

    def __str__(self):
        return self.provinceName

    class Meta:
        verbose_name = "省份"
        verbose_name_plural = "省份"


@python_2_unicode_compatible
class Area(models.Model):
    areaId = models.AutoField(primary_key=True)
    provinceId = models.ForeignKey(Province)
    areaName = models.CharField(max_length=20)
    isShow = models.BooleanField("是否启用", choices=yes_or_no, default=True)

    def __str__(self):
        return self.areaName

    class Meta:
        verbose_name = "地区"
        verbose_name_plural = "地区"


@python_2_unicode_compatible
class User(models.Model):
    userId = models.CharField(max_length=36, primary_key=True)
    areaId = models.ForeignKey(Area, blank=True, null=True)
    userName = models.CharField(max_length=11)
    userPwd = models.CharField(max_length=90)
    registerTime = models.DateTimeField(auto_now_add=True)
    remark = models.TextField(blank=True, null=True)  # 备注
    isShow = models.BooleanField("是否启用", choices=yes_or_no, default=True)
    loginTime = models.DateTimeField(auto_now_add=True, blank=True, null=True)  # 最近一次登录时间
    userPic = models.CharField(max_length=200, blank=True, null=True)  # 用户照片
    userEmail = models.CharField(max_length=50)
    userPhone = models.CharField(max_length=20, blank=True, null=True)
    userSex = models.BooleanField(default=1)

    def __str__(self):
        return self.userName

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = "用户"


@python_2_unicode_compatible
class Address(models.Model):
    addId = models.CharField(max_length=36, primary_key=True)
    userId = models.ForeignKey(User)
    areaId = models.ForeignKey(Area)
    addressInfor = models.CharField(max_length=200)  # 收货详细地址
    isShow = models.BooleanField("是否启用", choices=yes_or_no, default=True)
    isDefault = models.BooleanField()  # 是否是默认地址
    addPeople = models.CharField(max_length=20)  # 收货联系人
    addPhone = models.CharField(max_length=20)  # 联系电话
    createTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.userId.userName + self.addressInfor

    class Meta:
        verbose_name = "收货地址"
        verbose_name_plural = "收货地址"







