# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

yes_or_no = (
    (True, "是"),
    (False, "否")
)


@python_2_unicode_compatible
class ParentProductClass(models.Model):
    parentProductClassId = models.AutoField(primary_key=True)
    parentName = models.CharField(max_length=20)  # 商品父类名称
    isShow = models.BooleanField("是否启用", choices=yes_or_no, default=True)  # 是否启用

    def __str__(self):
        return self.parentName


@python_2_unicode_compatible
class ProductClass(models.Model):
    productClassId = models.AutoField(primary_key=True)
    parentProductClassId = models.ForeignKey(ParentProductClass)  # 商品类型所属父类
    className = models.CharField(max_length=20)  # 商品类型名称
    isShow = models.BooleanField("是否启用", choices=yes_or_no, default=True)
    createTime = models.DateTimeField(auto_now_add=True)  # 创建时间

    def __str__(self):
        return self.className


@python_2_unicode_compatible
class Material(models.Model):
    materialId = models.AutoField(primary_key=True)
    materialName = models.CharField(max_length=20)  # 材质名称
    isShow = models.BooleanField("是否启用", choices=yes_or_no, default=True)
    createTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.materialName


@python_2_unicode_compatible
class Colors(models.Model):
    colorId = models.AutoField(primary_key=True)
    colorName = models.CharField(max_length=32)
    createTime = models.DateTimeField(auto_now_add=True)
    isShow = models.BooleanField("是否启用", choices=yes_or_no, default=True)

    def __str__(self):
        return self.colorName


@python_2_unicode_compatible
class Product(models.Model):
    productId = models.CharField(max_length=36, primary_key=True)
    productClassId = models.ForeignKey(ProductClass)  # 所属商品类
    productName = models.CharField(max_length=50)
    productPrice = models.DecimalField(max_digits=20, decimal_places=2)
    productRemainder = models.IntegerField()   # 商品库存/余量
    productIntroduction = models.TextField(blank=True, null=True)
    isRecommendation = models.BooleanField(default=1)  # 是否推荐
    isShow = models.BooleanField("是否启用", choices=yes_or_no, default=True)
    picture = models.CharField(max_length=300, default=0, blank=True, null=True)
    miniPicture = models.CharField(max_length=300, default=0, blank=True, null=True)
    createTime = models.DateTimeField(auto_now_add=True)
    productInfo = models.TextField(blank=True, null=True)  # 商品详细信息

    def __str__(self):
        return self.productName


@python_2_unicode_compatible
class ProductAndColor(models.Model):
    productAndColorId = models.CharField(max_length=36, primary_key=True)
    productId = models.ForeignKey(Product)
    colorId = models.ForeignKey(Colors)
    isDefault = models.BooleanField("是否默认", choices=yes_or_no)

    def __str__(self):
        return self.productAndColorId