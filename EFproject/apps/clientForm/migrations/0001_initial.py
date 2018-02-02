# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-10-23 16:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientID', models.CharField(max_length=12, verbose_name='clientID')),
                ('firstName', models.CharField(max_length=25, verbose_name='firstName')),
                ('lastName', models.CharField(max_length=25, verbose_name='lastName')),
                ('postCode', models.CharField(max_length=25, verbose_name='postCode')),
                ('status', models.CharField(default='Open', max_length=10, verbose_name='status')),
                ('caseWorker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='caseWorker')),
            ],
            options={
                'verbose_name': 'ClientInfo',
                'verbose_name_plural': 'ClientInfo',
            },
        ),
    ]
