# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from admina.models import Product, ProductAndColor
from users.models import User

yes_or_no = (
    (True, "是"),
    (False, "否")
)


@python_2_unicode_compatible
class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.nmae

@python_2_unicode_compatible
class Trolley(models.Model):
    trolleyId = models.CharField(max_length=36, primary_key=True)
    productId = models.ForeignKey(Product)  # 商品表
    userId = models.ForeignKey(User)  # 用户表
    colorId = models.ForeignKey(ProductAndColor, blank=True, null=True)  # 颜色表
    number = models.IntegerField()  # 数量
    productPrice = models.DecimalField(max_digits=20, decimal_places=2)  # 商品价格
    createDate = models.DateTimeField(auto_now_add=True)  # 购买日期
    status = models.IntegerField(default=0)  # 当前加入状态  0 加入购物车; 1 生成订单; -1 删除

    def __str__(self):
        return self.trolleyId

