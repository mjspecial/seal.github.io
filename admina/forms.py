# -*- coding: utf-8 -*-
from django import forms


class LoginForm(forms.Form):
    userName = forms.CharField(max_length=20,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'weui-input',
                                                             'name': 'userName'}),
                               error_messages={'required': "用户名不能为空"})
    passWord = forms.CharField(max_length=20,
                              required=True,
                              widget=forms.PasswordInput(attrs={'class': 'weui-input',
                                                                'name': 'passWord'}),
                              error_messages={'required': "密码不能为空"})
    vcode = forms.CharField(widget=forms.TextInput(attrs={'class': 'weui-input',
                                                             'name': 'vcode'}),
                            required=True,
                            max_length=4,
                            error_messages={'required': "验证码不能为空"}
                            )

    def clean_userName(self):
        un = self.cleaned_data['userName']
        if un == '12':
            raise forms.ValidationError('用户名已存在')
        return self.cleaned_data['userName']