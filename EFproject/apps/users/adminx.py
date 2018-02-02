# _*_ coding: utf-8 _*_
__author__ = 'Di Meng'
__date__ = '9/26/2017 2:45 PM'


import xadmin
from xadmin import views
from .models import EmailVerifyRecord


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "EngageFirst Dashboard Backend Management"
    site_footer = "EngageFirst"
    menu_style = "accordion"


class EmailVerifyRecordAdmin(object):
    # display list of columns
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


# class BannerAdmin(object):
#     list_display = ['title', 'image', 'url', 'index', 'add_time']
#     search_fields = ['title', 'image', 'url', 'index']
#     list_filter = ['title', 'image', 'url', 'index', 'add_time']

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)