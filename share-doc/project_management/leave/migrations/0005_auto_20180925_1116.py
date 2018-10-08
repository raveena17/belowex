# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-09-25 11:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0004_auto_20180925_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='approved_by',
            field=models.ForeignKey(db_column='approved_by', on_delete=django.db.models.deletion.CASCADE, related_name='leave_request_approved_by', to=settings.AUTH_USER_MODEL, verbose_name='approved_by'),
        ),
    ]
