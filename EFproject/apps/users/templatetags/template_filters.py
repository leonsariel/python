# _*_ coding: utf-8 _*_
__author__ = 'Di Meng'
__date__ = '11/8/2017 11:38 AM'


from django.template.defaulttags import register
@register.filter


def getItemLength(dictionary, key):

    return len(dictionary.get(key))

def key(d, key_name):
    return d[key_name]
key = register.filter('key', key)