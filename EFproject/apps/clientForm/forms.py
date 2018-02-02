# _*_ coding: utf-8 _*_
__author__ = 'Di Meng'
__date__ = '10/17/2017 10:21 AM'
from django import forms

class ClientForm1(forms.Form):
    clientID = forms.CharField(required=True)
    firstName = forms.CharField(required=True)
    lastName = forms.CharField(required=True)
    postCode = forms.CharField(required=True, min_length=6)
    status = forms.ChoiceField(required=True)


class ClientForm2(forms.Form):
    knob = forms.CharField(required=True)
    knob2 = forms.CharField(required=True)
    knob3 = forms.CharField(required=True)
    knob4 = forms.CharField(required=True)