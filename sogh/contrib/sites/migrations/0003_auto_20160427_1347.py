# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 13:47
from __future__ import unicode_literals

import django.contrib.sites.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_set_site_domain_and_name'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='site',
            managers=[
                ('objects', django.contrib.sites.models.SiteManager()),
            ],
        ),
        migrations.AlterField(
            model_name='site',
            name='domain',
            field=models.CharField(max_length=100, unique=True, validators=[django.contrib.sites.models._simple_domain_name_validator], verbose_name='domain name'),
        ),
    ]
