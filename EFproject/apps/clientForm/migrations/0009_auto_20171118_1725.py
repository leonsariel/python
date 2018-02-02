# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-11-19 00:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientForm', '0008_auto_20171118_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientinfo',
            name='region',
            field=models.CharField(choices=[('Calgary', 'Calgary'), ('Edmonton', 'Edmonton'), ('North', 'North'), ('South', 'South')], max_length=20),
        ),
        migrations.AlterField(
            model_name='clientinfo',
            name='site',
            field=models.CharField(choices=[('Calgary 251', 'Calgary 251'), ('Edmonton 300', 'Edmonton 300'), ('Edmonton 111', 'Edmonton 111'), ('North 92', 'North 92'), ('South 120', 'South 120')], max_length=20),
        ),
    ]