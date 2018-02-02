# _*_ encoding:utf-8 _*_
from django.db import models
from users.models import UserProfile
# Create your models here.


class ClientInfo(models.Model):
    clientID = models.CharField(max_length=12,verbose_name="clientID")
    caseWorker = models.ForeignKey(UserProfile, verbose_name="caseWorker")
    firstName = models.CharField(max_length=25, verbose_name="firstName")
    lastName = models.CharField(max_length=25, verbose_name="lastName")
    postCode = models.CharField(max_length=25, verbose_name="postCode")

    region = models.CharField(max_length=20,
                              choices=(("Calgary", "Calgary"), ("Edmonton", "Edmonton"), ("North", "North"),
                                       ("South", "South")))
    site = models.CharField(max_length=20, choices=(
    ("Calgary 100", "Calgary 100"), ("Calgary 200", "Calgary 200"), ("Edmonton 100", "Edmonton 100"), ("Edmonton 200", "Edmonton 200"),
    ("North 92", "North 92"),
    ("South 120", "South 120")))

    status = models.CharField(default="open not assigned",verbose_name="status",max_length=30,choices=(("open and assigned","open and assigned"),("open not assigned","open not assigned"),("onhold","onhold"),("closed","closed")))
    processStep = models.CharField(max_length=20, choices=(
        ("Intake", "Intake"), ("Assessor", "Assessor"), ("Case Manager", "Case Manager"),
        ("Generalist", "Generalist"),("Permanenty Worker","")), default="Intake")
    knob = models.CharField(max_length=3,verbose_name="knob",default="40%")
    knob2 = models.CharField(max_length=3, verbose_name="knob2",default="40%")
    knob3 = models.CharField(max_length=3, verbose_name="knob3",default="40%")
    knob4 = models.CharField(max_length=3, verbose_name="knob4",default="40%")


    # def _get_total(self):
    #     total = self.knob * 0.15 + self.knob2 * 0.35 + self.knob3 * 0.20 + self.knob4 * 0.30
    #     if (total < 20):
    #         return "low";
    #     elif (total >= 20 and total < 80):
    #         return "Avg";
    #     elif (total >= 80):
    #         return "high";
    # rating = property(_get_total,)
    rating = models.CharField(max_length=10, verbose_name="rating")
    class Meta:
        verbose_name = "ClientInfo"
        verbose_name_plural = verbose_name


class CaseIntensityRating(models.Model):
    clientID = models.CharField(max_length=12,verbose_name="clientID")
    knob = models.CharField(max_length=3,verbose_name="knob")
    knob2 = models.CharField(max_length=3, verbose_name="knob2")
    knob3 = models.CharField(max_length=3, verbose_name="knob3")
    knob4 = models.CharField(max_length=3, verbose_name="knob4")
    rating = models.CharField(max_length=10, verbose_name="rating",default="low")

    class Meta:
        verbose_name = "CIR"
        verbose_name_plural = verbose_name