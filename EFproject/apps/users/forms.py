# _*_ coding: utf-8 _*_
__author__ = 'Di Meng'
__date__ = '9/19/2017 10:34 AM'
from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField()


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField()


class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)


class UserInfoForm(forms.Form):
    userFirstName = forms.CharField(required=True, max_length=20)
    userLastName = forms.CharField(required=True, max_length=20)
    userPostCode = forms.CharField(required=True, min_length = 6)
    program = forms.CharField(required=True)
    # role = forms.ChoiceField(required=True)
    # reportTo = forms.ChoiceField(required=True)