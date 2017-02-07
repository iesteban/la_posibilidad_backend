# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0003_auto_20170123_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='balance_dest',
            field=models.IntegerField(help_text='Value of the wallet at the time of this transaction'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='balance_source',
            field=models.IntegerField(blank=True, 
                default=0, 
                help_text='Value of the wallet at the time of this transaction'
            ),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='balance',
            field=models.IntegerField(help_text='Available seeds in wallet'),
        ),
    ]
