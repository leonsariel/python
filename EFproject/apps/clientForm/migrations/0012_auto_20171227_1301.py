# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-12-27 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientForm', '0011_clientinfo_processstep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientinfo',
            name='site',
            field=models.CharField(choices=[('Calgary 100', 'Calgary 100'), ('Calgary 200', 'Calgary 200'), ('Edmonton 100', 'Edmonton 100'), ('Edmonton 200', 'Edmonton 200'), ('North 92', 'North 92'), ('South 120', 'South 120')], max_length=20),
        ),
    ]
