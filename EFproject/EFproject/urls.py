from django.conf.urls import url, include
from django.contrib import admin
from EFproject.settings import MEDIA_ROOT
from django.views.static import serve
from clientForm.views import ClientInfoView, SelectClientView, EditClientView
from django.views.generic import TemplateView
from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyPwdView, LogoutView, \
    IndexView, UserInfoView, SelectUserView
from clientForm.forms import ClientForm1, ClientForm2

import xadmin

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),

    url('^$', LoginView.as_view(), name="login"),
    url('^base/$', TemplateView.as_view(template_name="base.html"), name="base"),

    url(r'^index/$', IndexView.as_view(), name="index"),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^register/$', RegisterView.as_view(), name="register"),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name="user_active"),
    url(r'^forget/$', ForgetPwdView.as_view(), name="forget_pwd"),
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name="reset_pwd"),
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name="modify_pwd"),
    url('^select/$', RegisterView.as_view(), name="select"),

    url(r'^new/$', TemplateView.as_view(template_name="new.html"), name="new"),
    url(r'^allocation/$', TemplateView.as_view(template_name="allocation.html"), name="new"),
    url(r'^test/$', TemplateView.as_view(template_name="test.html"), name="test"),

    url(r'^new_cir/$', ClientInfoView.as_view(), name="new_cir"),
    url(r'^selectClient/$', SelectClientView.as_view(), name="selectClient"),
    url(r'^editClient/$', EditClientView.as_view(), name="editClient"),
    url(r'^userInfo/$', UserInfoView.as_view(), name="userInfo"),
    url(r'^selectUser/$', SelectUserView.as_view(), name="selectUser"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),

]
