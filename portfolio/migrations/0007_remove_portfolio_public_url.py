# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-03 12:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_portfolio_public_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='public_url',
        ),
    ]
