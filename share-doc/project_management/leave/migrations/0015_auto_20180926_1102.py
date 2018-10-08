# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-09-26 11:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0014_auto_20180925_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='status',
            name='empid',
            field=models.ForeignKey(db_column='empid', on_delete=django.db.models.deletion.CASCADE, related_name='leave_status_empid', to='leave.Request', verbose_name='empid'),
        ),
        migrations.AlterModelTable(
            name='type',
            table='leavetype',
        ),
    ]
