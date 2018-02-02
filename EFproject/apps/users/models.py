# _*_ coding: utf-8 _*_
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


# Create your models here.


class UserProfile(AbstractUser):
    isRegister = models.BooleanField(default=False)
    firstName = models.CharField(max_length=50, verbose_name="firstName", default="")
    lastName = models.CharField(max_length=50, verbose_name="lastName", default="")
    # gender = models.CharField(max_length=6 ,choices=(("male","male"),("female","female")),default="male")
    region = models.CharField(max_length=20,
                              choices=(("Calgary", "Calgary"), ("Edmonton", "Edmonton"), ("North", "North"),
                                       ("South", "South")))
    site = models.CharField(max_length=20, choices=(
    ("Calgary 100", "Calgary 100"), ("Calgary 200", "Calgary 200"), ("Edmonton 100", "Edmonton 100"), ("Edmonton 200", "Edmonton 200"),
    ("North 92", "North 92"),
    ("South 120", "South 120")))
    postCode = models.CharField(max_length=6, default="")
    # address = models.CharField(max_length=100, default="")
    # site = models.CharField(max_length=100, default="")
    role = models.CharField(max_length=20, choices=(
    ("Case Worker", "Case Worker"), ("Supervisor", "Supervisor"), ("Manager", "Manager"),
    ("Regional Director", "Regional Director")), default="Supervisor")

    processStep = models.CharField(max_length=20, choices=(
        ("Intake", "Intake"), ("Assessor", "Assessor"), ("Case Manager", "Case Manager"),
        ("Generalist", "Generalist"),("Permanenty Worker","")), default="Intake")

    image = models.ImageField(upload_to="image/%y/%m", default="image/default.png", max_length=100)
    reportTo = models.CharField(max_length=30, verbose_name="reportTo", default="")
    program = models.CharField(default="OPG", verbose_name="program", max_length=30,
                               choices=(("OPG", "OPG"), ("OPT", "OPT")))

    class Meta:
        verbose_name = "userInfo"
        verbose_name_plural = "userInfo"

    def __unicode__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name="code")
    email = models.EmailField(max_length=50, verbose_name="email")
    send_type = models.CharField(max_length=10, choices=(("register", "register"), ("forget", "forget")))
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "emailVerification"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)
